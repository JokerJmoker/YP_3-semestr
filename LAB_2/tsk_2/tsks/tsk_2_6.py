from vectors_math import Vector, math
from itertools import combinations


def calc_distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2)


def calc_perimeter_between_3_points(point1, point2, point3):
    return (calc_distance(point1, point2) + calc_distance(point2, point3) + calc_distance(point3, point1))


def find_max_perimeter(points):
    """Находит максимальный периметр треугольника, образованного тремя точками"""
    max_perimeter = 0
    max_triangle = None
    
    for p1, p2, p3 in combinations(points, 3):
        current_perimeter = calc_perimeter_between_3_points(p1, p2, p3)
        if current_perimeter > max_perimeter:
            max_perimeter = current_perimeter
            max_triangle = (p1, p2, p3)
    
    return f' {max_perimeter:.2f} '


def tsk_2_6():
    number_of_points = int(input("Введите количество точек: "))
    text = 'Максимальный периметр треугольника: '
    result = Vector.get_result_for_several_points(number_of_points, find_max_perimeter, text)
    print(result)
