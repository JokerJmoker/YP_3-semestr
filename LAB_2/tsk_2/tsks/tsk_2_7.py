from vectors_math import Vector, math
from itertools import combinations


def vector_from_points(p1, p2):
    return Vector(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)


def triangle_area(p1, p2, p3):
    vec1 = vector_from_points(p1, p2)
    vec2 = vector_from_points(p1, p3)
    cross_prod = Vector.cross_product(vec1, vec2)
    area = 0.5 * math.sqrt(cross_prod.x**2 + cross_prod.y**2 + cross_prod.z**2)
    return area


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