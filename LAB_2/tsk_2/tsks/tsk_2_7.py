from vectors_math import Vector
import math
from itertools import combinations

def cross_product(vec1, vec2):
    """Вычисляет векторное произведение двух векторов"""
    x = vec1.y * vec2.z - vec1.z * vec2.y
    y = vec1.z * vec2.x - vec1.x * vec2.z
    z = vec1.x * vec2.y - vec1.y * vec2.x
    return Vector(x, y, z)

def vector_from_points(p1, p2):
    """Создает вектор из двух точек"""
    return Vector(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)

def triangle_area(p1, p2, p3):
    """Вычисляет площадь треугольника, образованного тремя точками"""
    vec1 = vector_from_points(p1, p2)
    vec2 = vector_from_points(p1, p3)
    cross_prod = cross_product(vec1, vec2)
    area = 0.5 * math.sqrt(cross_prod.x**2 + cross_prod.y**2 + cross_prod.z**2)
    return area

def find_max_area(points):
    """Находит максимальную площадь треугольника, образованного тремя точками"""
    max_area = 0
    
    for p1, p2, p3 in combinations(points, 3):
        current_area = triangle_area(p1, p2, p3)
        if current_area > max_area:
            max_area = current_area
    
    return max_area

def get_result_tsk_2_7():
    """Запрашивает у пользователя точки и находит треугольник с максимальной площадью"""
    N = int(input("Введите количество точек: "))
    points = []
    
    for _ in range(N):
        coords = input("Введите координаты точки (x,y,z): ")
        points.append(Vector(coords))
    
    max_area = find_max_area(points)
    return f'Максимальная площадь треугольника: {max_area}'

def tsk_2_7():
    result = get_result_tsk_2_7()
    print(result)
