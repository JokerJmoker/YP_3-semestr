import numpy as np

ik = -5 -2j
e2 = -550 + 320j
e3 = 400 - 200j
e6 = 240 + 20j

z1 = -40j
z2 = 30j
z4 = 20 + 90j
z5 = 70 - 20j
z6 = -20j

# Создаем комплексную матрицу 5x5
matrix_R = np.array([
    [-1, -1, 0, 0, 0],
    [0, 1, -1, -1, 0],
    [1, 0, 0, 1, -1],
    [-z4, z6, z2, 0, 0],
    [0, 0, -z2, z5, 0]
])

# Создаем матрицу E (5x1)
matrix_E = np.array([
    [-ik],
    [0],
    [0],
    [e3+e6+e2],
    [-e3-e2]
])

# Проверяем, является ли матрица R обратимой (детерминант не равен нулю)
det = np.linalg.det(matrix_R)

if det == 0:
    print("Матрица R необратима")
else:
    # Находим обратную матрицу R
    inverse_matrix_R = np.linalg.inv(matrix_R)

    # Настройка формата вывода для комплексных чисел
    np.set_printoptions(precision=3, suppress=True)

    print("Обратная матрица R:")
    for row in inverse_matrix_R:
        formatted_row = ["{0.real:.4f}{0.imag:+.4f}j".format(x) for x in row]
        print("  ".join(formatted_row))

    # Умножаем матрицу E на обратную матрицу R справа
    result = np.dot(inverse_matrix_R, matrix_E)

    print("\nРезультат умножения матрицы E на обратную матрицу R:")
    for row in result:
        print("{0.real:.4f}{0.imag:+.4f}j".format(row[0]))
