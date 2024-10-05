from argparse import ArgumentParser # позволяет обрабатывать аргументы командной строки.
import json
import time

from utils import Norm, normalize_angle, argmax # argmax  возвращает индекс элемента с наибольшим значением из списка вероятностей.

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
    """
    Используется argparse.ArgumentParser для того, чтобы получить три аргумента из командной строки:
    graph: путь к файлу с графом переходов частиц.
    config: имя файла конфигурации локализации, содержащего параметры начальной позиции и движения.
    out: путь к выходному файлу для записи сгенерированной траектории.
    """
    parser = ArgumentParser(description="Generate trajectory with Viterbi algorithm")
    parser.add_argument("graph", help="path to particle transition graph files")
    parser.add_argument("config", help="localization config name")
    parser.add_argument("out", help="path to output file")
    args = parser.parse_args()

    # Read configuration and prepare distributions  Чтение конфигурации:
    with open(args.config) as f:
        config = json.load(f)
        # начальные позиции 
        x_mu, y_mu = config["initial_position"]
        h_mu = config["initial_heading"]
        # отклонения 
        x_dist = Norm(mu=x_mu, std=config["init_position_stddev"])
        y_dist = Norm(mu=y_mu, std=config["init_position_stddev"])
        h_dist = Norm(mu=h_mu, std=config["init_heading_stddev"])
        # Параметры движения motion_params, которые используются для моделирования переходов частиц.
        mot_params = config["motion_params"]
        # создаются распределения
        get_prob = (lambda x, y, h:
                    get_cumulative_probability(x, y, h,
                                               x_dist, y_dist, h_dist))

    # Read graph Чтение графа переходов
    graph = []
    with open(args.graph) as f:# Загружается граф переходов из файла graph
        for line in f:
            graph.append(json.loads(line))

    # Prepare arrays for solving problem with dynamic programming (DP)
    # prev - array for path recovery
    # prob - array, that contains probability of each particle for each time
    # prob[0] is initialized using initial particles weights and probability of their position
    """
    Подготовка массивов для динамического программирования:

    prev — массив для восстановления пути. Хранит индекс предыдущей частицы, 
    из которой был сделан наилучший переход.

    prob — массив для хранения вероятностей каждого состояния на каждом шаге времени. 
    Вероятности инициализируются для первого шага, используя начальные вероятности частиц.
    """
    
    total_steps = len(graph)
    prev = [[-1] * len(graph[0]["particles"]["x"])]
    prob = [[get_prob(x, y, h) * w for x, y, h, w in zip(graph[0]["particles"]["x"],
                                                         graph[0]["particles"]["y"],
                                                         graph[0]["particles"]["heading"],
                                                         graph[0]["particles"]["weight"])]]

    # Start Viterbi algorithm

    start = time.time()
    for step in range(1, total_steps):
        
        data_cur = graph[step]["particles"]
        data_prev = graph[step - 1]["particles"]
        delta_x = graph[step]["delta_odometry"]["position"]["x"]
        delta_y = graph[step]["delta_odometry"]["position"]["y"]
        delta_h = graph[step]["delta_odometry"]["heading"]
        prev.append([-1] * len(data_cur["x"]))
        prob.append([0] * len(data_cur["x"]))
        """
        Происходит итерация по каждому шагу времени, начиная со второго. 
        Для каждой частицы на текущем шаге вычисляется вероятность перехода 
        из каждой частицы на предыдущем шаге.
        """
        # Iterate over each particle for current time moment
        for i, x_c, y_c, h_c, w_c in zip(range(len(data_cur["x"])), data_cur["x"],
                                         data_cur["y"], data_cur["heading"], data_cur["weight"]):
            # Iterate over each particle for previous time moment
            """
            Для каждой частицы на предыдущем шаге вызывается функция get_transition_probability,
              которая вычисляет вероятность перехода из положения p в положение q с учётом движения 
              (delta_x, delta_y, delta_h).
            """
            for j, x_p, y_p, h_p in zip(range(len(data_prev["x"])), data_prev["x"],
                                        data_prev["y"], data_prev["heading"]):
                tran_prob = get_transition_probability((x_p, y_p, h_p), (x_c, y_c, h_c),
                                                       (delta_x, delta_y, delta_h), mot_params)
                if prob[step][i] < w_c * tran_prob * prob[step - 1][j]:
                    prob[step][i] = w_c * tran_prob * prob[step - 1][j]
                    prev[step][i] = j
        # Now sum of probabilities can be not equal to 1, so we're normalizing them
        """
        После каждой итерации вероятности нормализуются, чтобы их сумма была равна 1.
        """
        s = sum(prob[step])
        prob[step] = [x / s for x in prob[step]]
    print(time.time() - start)

    # Recover trajectory using DP path recovery method Восстановление траектории:
    """
    После завершения алгоритма Витерби программа использует
    массив prev для восстановления пути назад от последней частицы.
    """
    j = argmax(prob[-1])
    idx_path = []
    i = len(graph) - 1
    while j != -1:
        idx_path.append(j)
        j = prev[i][j]
        i -= 1
    trajectory = []
    """
    Восстановленный путь сохраняется в виде 
    последовательности координат частиц (их x, y и heading).
    """
    for i, j in enumerate(idx_path[::-1]):
        trajectory.append((
            graph[i]["particles"]["x"][j],
            graph[i]["particles"]["y"][j],
            graph[i]["particles"]["heading"][j]
        ))

    # Let's write an answer to json file
    with open(args.out, "w") as f:
        json.dump(trajectory, f)
