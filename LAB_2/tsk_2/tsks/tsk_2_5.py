from vectors_math import Vector
import math

def cross_product(vec1, vec2):
    """Вычисляет векторное произведение двух векторов"""
    x = vec1.y * vec2.z - vec1.z * vec2.y
    y = vec1.z * vec2.x - vec1.x * vec2.z
    z = vec1.x * vec2.y - vec1.y * vec2.x
    return Vector(x, y, z)

def dot_product(vec1, vec2):
    """Вычисляет скалярное произведение двух векторов"""
    return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z

def parallelepiped_volume(vec1, vec2, vec3):
    """Вычисляет объем параллелепипеда, построенного на трех векторах"""
    cross_prod = cross_product(vec2, vec3)
    volume = abs(dot_product(vec1, cross_prod))
    return volume

def get_result_tsk_2_5():
    """Запрашивает у пользователя три вектора и вычисляет объем параллелепипеда"""
    coords1 = input("Введите координаты первого вектора (x,y,z): ")
    vec1 = Vector(coords1)
    
    coords2 = input("Введите координаты второго вектора (x,y,z): ")
    vec2 = Vector(coords2)
    
    coords3 = input("Введите координаты третьего вектора (x,y,z): ")
    vec3 = Vector(coords3)
    
    volume = parallelepiped_volume(vec1, vec2, vec3)
    return f'Объем параллелепипеда: {volume}'

def tsk_2_5():
    result = get_result_tsk_2_5()
    print(result)