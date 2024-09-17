from vectors_math import Vector

def find_center_of_mass(points):
    """Находит и возвращает координаты центра масс для множества точек"""
    if not points:
        return None

    total_vector = Vector(0, 0, 0) # вектор, к которму суммируются все отсальные
    
    for point in points:
        total_vector += point

    center_of_mass = total_vector / len(points)
    return center_of_mass

def tsk_2_3():
    number_of_points = int(input("Введите количество точек: "))
    text = 'Координаты центра масс данного множетсва точек: '
    result = Vector.get_result_for_several_points(number_of_points, find_center_of_mass, text)
    print(result)