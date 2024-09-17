from vectors_math import Vector, math



def calc_parallelogram_area(vec1, vec2):
    cross_prod = Vector.cross_product(vec1, vec2)
    area = math.sqrt(cross_prod.x**2 + cross_prod.y**2 + cross_prod.z**2)
    return area

def get_area():
    vec1 = Vector.input_vector('Введите координаты первого вектора (x,y,z): ')
    vec2 = Vector.input_vector('Введите координаты второго вектора (x,y,z): ')
    area = calc_parallelogram_area(vec1, vec2)
    return f'Площадь параллелограмма: {area:.2f}'

def tsk_2_4():
    result = get_area()
    print(result)
