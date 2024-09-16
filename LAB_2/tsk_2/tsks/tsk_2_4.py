from vectors_math import Vector
import math

def cross_product(vec1, vec2):
    """Вычисляет векторное произведение двух векторов"""
    x = vec1.y * vec2.z - vec1.z * vec2.y
    y = vec1.z * vec2.x - vec1.x * vec2.z
    z = vec1.x * vec2.y - vec1.y * vec2.x
    return Vector(x, y, z)

def parallelogram_area(vec1, vec2):
    """Вычисляет площадь параллелограмма, построенного на двух векторах"""
    cross_prod = cross_product(vec1, vec2)
    # Модуль векторного произведения
    area = math.sqrt(cross_prod.x**2 + cross_prod.y**2 + cross_prod.z**2)
    return area

def get_result_tsk_2_4():
    """Запрашивает у пользователя два вектора и вычисляет площадь параллелограмма"""
    coords1 = input("Введите координаты первого вектора (x,y,z): ")
    vec1 = Vector(coords1)
    
    coords2 = input("Введите координаты второго вектора (x,y,z): ")
    vec2 = Vector(coords2)
    
    area = parallelogram_area(vec1, vec2)
    return f'Площадь параллелограмма: {area:.2f}'

def tsk_2_4():
    result = get_result_tsk_2_4()
    print(result)
