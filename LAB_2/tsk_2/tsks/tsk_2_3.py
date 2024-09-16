from vectors_math import Vector

def find_center_of_mass(points):
    """Находит и возвращает координаты центра масс для множества точек"""
    if not points:
        return None

    total_vector = Vector(0, 0, 0)
    
    for point in points:
        total_vector += point

    # Центр масс — это среднее арифметическое координат всех точек
    center_of_mass = total_vector / len(points)
    return center_of_mass

def get_result_tsk_2_3(N):
    points = []
    
    for _ in range(N):
        coords = input("Введите координаты точки (x,y,z): ")
        points.append(Vector(coords))

    center_of_mass = find_center_of_mass(points)
    return f'Координаты центра масс: {center_of_mass}'

def tsk_2_3():
    N = int(input("Введите количество точек: "))
    result = get_result_tsk_2_3(N)
    print(result)
