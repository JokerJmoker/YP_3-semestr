from vectors_math import Vector, math
from itertools import combinations


def triangle_area(vec1, vec2, vec3):
    """Вычисляет площадь треугольника, образованного тремя точками"""
    AB = vec2 - vec1
    AC = vec3 - vec1
    cross_prod = Vector.cross_product(AB, AC)
    return 0.5 * math.sqrt(cross_prod.x**2 + cross_prod.y**2 + cross_prod.z**2)


def find_max_area(points):
    max_area = 0
    for p1, p2, p3 in combinations(points, 3):
        current_area = triangle_area(p1, p2, p3)
        if current_area > max_area:
            max_area = current_area
    return f'{max_area:.2f}'


def tsk_2_7():
    number_of_points = int(input("Введите количество точек: "))
    text = 'Максимальная площадь треугольника: '
    result = Vector.get_result_for_several_points(number_of_points, find_max_area, text)
    print(result)