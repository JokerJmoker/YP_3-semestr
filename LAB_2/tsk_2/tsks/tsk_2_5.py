from vectors_math import Vector


def calc_parallelepiped_volume(vec1, vec2, vec3):
    cross_prod = Vector.cross_product(vec2, vec3)
    volume = abs(Vector.dot_product(vec1, cross_prod))
    return volume


def get_volume():
    vec1 = Vector.input_vector('Введите координаты первого вектора (x,y,z): ')
    vec2 = Vector.input_vector('Введите координаты второго вектора (x,y,z): ')
    vec3 = Vector.input_vector('Введите координаты третьего вектора (x,y,z): ')
    volume = calc_parallelepiped_volume(vec1, vec2, vec3)
    return f'Объем параллелепипеда: {volume}'


def tsk_2_5():
    result = get_volume()
    print(result)