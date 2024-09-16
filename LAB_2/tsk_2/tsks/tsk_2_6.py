from vectors_math import Vector
import math
from itertools import combinations

def distance(point1, point2):
    """Вычисляет расстояние между двумя точками"""
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2)

def perimeter(point1, point2, point3):
    """Вычисляет периметр треугольника, образованного тремя точками"""
    return (distance(point1, point2) +
            distance(point2, point3) +
            distance(point3, point1))

def find_max_perimeter(points):
    """Находит максимальный периметр треугольника, образованного тремя точками"""
    max_perimeter = 0
    max_triangle = None
    
    for p1, p2, p3 in combinations(points, 3):
        current_perimeter = perimeter(p1, p2, p3)
        if current_perimeter > max_perimeter:
            max_perimeter = current_perimeter
            max_triangle = (p1, p2, p3)
    
    return max_perimeter

def get_result_tsk_2_6():
    """Запрашивает у пользователя точки и находит треугольник с максимальным периметром"""
    N = int(input("Введите количество точек: "))
    points = []
    
    for _ in range(N):
        coords = input("Введите координаты точки (x,y,z): ")
        points.append(Vector(coords))
    
    max_perim = find_max_perimeter(points)
    return f'Максимальный периметр треугольника: {max_perim}'

def tsk_2_6():
    result = get_result_tsk_2_6()
    print(result)
