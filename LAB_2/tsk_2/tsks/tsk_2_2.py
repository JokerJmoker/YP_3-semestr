from vectors_math import Vector  

def find_farthest_point(points):
    """Находит и возвращает точку, наиболее удаленную от начала координат"""
    farthest_point = None
    max_distance = -1
    
    for point in points:
        distance = point.distance_from_origin()
        if distance > max_distance:
            max_distance = distance
            farthest_point = point
    
    return farthest_point

def get_result_tsk_2_2(N):
    """Запрашивает координаты точек и возвращает строку с наиболее удаленной точкой"""
    points = []
    for _ in range(N):
        coords = input("Введите координаты точки (x,y,z): ")
        points.append(Vector(coords))

    farthest_point = find_farthest_point(points)
    return f'Наиболее удаленная точка от начала отсчета имеет следующие координаты: {farthest_point}'

def tsk_2_2():
    """Получает количество точек и выводит наиболее удаленную точку"""
    N = int(input("Введите количество точек: "))
    result = get_result_tsk_2_2(N)
    print(result)
