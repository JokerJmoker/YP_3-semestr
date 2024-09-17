from vectors_math import Vector, math


def find_farthest_point(points):
    """Находит и возвращает точку, наиболее удаленную от начала координат"""
    farthest_point = None
    max_distance = -1
    
    for point in points:
        distance = math.sqrt(point.x**2 + point.y**2 + point.z**2)
        if distance > max_distance:
            max_distance = distance
            farthest_point = point
    
    return farthest_point


def tsk_2_2():
    number_of_points = int(input("Введите количество точек: "))
    text = 'Наиболее удаленная точка от начала отсчета имеет координаты:'
    result = Vector.get_result_for_several_points(number_of_points, find_farthest_point, text)
    print(result)