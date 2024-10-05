import multiprocessing as mp
import time
from argparse import ArgumentParser
import json
from utils import Norm, normalize_angle, argmax

def compute_probabilities(i, data_cur, data_prev, delta_x, delta_y, delta_h, mot_params, prob_prev):
    x_c, y_c, h_c, w_c = data_cur
    max_prob = 0
    best_j = -1
    for j, x_p, y_p, h_p in data_prev:
        tran_prob = get_transition_probability((x_p, y_p, h_p), (x_c, y_c, h_c), (delta_x, delta_y, delta_h), mot_params)
        current_prob = w_c * tran_prob * prob_prev[j]
        if current_prob > max_prob:
            max_prob = current_prob
            best_j = j
    return i, max_prob, best_j


# вычисляет совокупную вероятность для трёх значений (координаты x, y и угол h) dish - распределение
def get_cumulative_probability(x: float, y: float, h: float,
                               x_dist: Norm, y_dist: Norm, h_dist: Norm) -> float:
    """
    Get cummulative probability for three independently distributed values.
    :param x: X-axis value
    :param y: Y-axis value
    :param h: heading value
    :param x_dist: X-axis values distribution
    :param y_dist: Y-axis values distribution
    :param h_dist: heading values distribution

    :returns: probability
    """
    return x_dist.pdf(x) * y_dist.pdf(y) * h_dist.pdf(h)

# вычисляет вероятность перехода из одного положения (p) в другое (q) с учётом движения
def get_transition_probability(p: tuple, q: tuple, delta: tuple, mot_params: dict) -> float:
    """
    Get probability of transition from one pose to another.
    :param p: initial pose
    :param q: target pose
    :param delta: inforamtion about movement
    :param mot_params: motion parameters

    :returns: probability
    """
    dist_l = Norm(mu=mot_params["linear"]["mean"], std=mot_params["linear"]["stddev"])
    dist_a = Norm(mu=mot_params["angular"]["mean"], std=mot_params["angular"]["stddev"])
    s = (delta[0] ** 2 + delta[1] ** 2) ** 0.5
    s_t = ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5
    if s == 0:
        x = 1
    else:
        p_l = (s_t - s) / s
        x = dist_l.pdf(p_l)
    p_a = normalize_angle(q[2] - p[2] - delta[2])
    y = dist_a.pdf(p_a)
    return x * y


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate trajectory with Viterbi algorithm")
    parser.add_argument("graph", help="path to particle transition graph files")
    parser.add_argument("config", help="localization config name")
    parser.add_argument("out", help="path to output file")
    args = parser.parse_args()

    # Read configuration and prepare distributions
    with open(args.config) as f:
        config = json.load(f)
        x_mu, y_mu = config["initial_position"]
        h_mu = config["initial_heading"]
        x_dist = Norm(mu=x_mu, std=config["init_position_stddev"])
        y_dist = Norm(mu=y_mu, std=config["init_position_stddev"])
        h_dist = Norm(mu=h_mu, std=config["init_heading_stddev"])
        mot_params = config["motion_params"]
        get_prob = (lambda x, y, h:
                    get_cumulative_probability(x, y, h,
                                               x_dist, y_dist, h_dist))

    # Read graph
    graph = []
    with open(args.graph) as f:
        for line in f:
            graph.append(json.loads(line))

    total_steps = len(graph)
    prev = [[-1] * len(graph[0]["particles"]["x"])]
    prob = [[get_prob(x, y, h) * w for x, y, h, w in zip(graph[0]["particles"]["x"],
                                                         graph[0]["particles"]["y"],
                                                         graph[0]["particles"]["heading"],
                                                         graph[0]["particles"]["weight"])]]


    start = time.time()
    
    pool = mp.Pool(mp.cpu_count())  # Создание пула процессов
    
    for step in range(1, total_steps):
        data_cur = list(zip(graph[step]["particles"]["x"],
                            graph[step]["particles"]["y"],
                            graph[step]["particles"]["heading"],
                            graph[step]["particles"]["weight"]))
        data_prev = list(zip(graph[step - 1]["particles"]["x"],
                             graph[step - 1]["particles"]["y"],
                             graph[step - 1]["particles"]["heading"]))
        delta_x = graph[step]["delta_odometry"]["position"]["x"]
        delta_y = graph[step]["delta_odometry"]["position"]["y"]
        delta_h = graph[step]["delta_odometry"]["heading"]
        prev.append([-1] * len(data_cur))
        prob.append([0] * len(data_cur))

        # Запуск параллельных вычислений для текущего шага
        results = pool.starmap(compute_probabilities, [(i, data_cur[i], data_prev, delta_x, delta_y, delta_h, mot_params, prob[step - 1]) for i in range(len(data_cur))])

        # Обработка результатов
        for i, max_prob, best_j in results:
            prob[step][i] = max_prob
            prev[step][i] = best_j

        # Нормализация вероятностей
        s = sum(prob[step])
        prob[step] = [x / s for x in prob[step]]
    
    print(time.time() - start)

    pool.close()  # Закрытие пула процессов
    pool.join()   # Ожидание завершения всех процессов

    # Восстановление траектории
    j = argmax(prob[-1])
    idx_path = []
    i = len(graph) - 1
    while j != -1:
        idx_path.append(j)
        j = prev[i][j]
        i -= 1
    trajectory = []
    for i, j in enumerate(idx_path[::-1]):
        trajectory.append((graph[i]["particles"]["x"][j],
                           graph[i]["particles"]["y"][j],
                           graph[i]["particles"]["heading"][j]))

    with open(args.out, "w") as f:
        json.dump(trajectory, f)
