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


# Матрица коэффициентов
A = np.array([
    [
        (1/z1 + 1/z4 + 1/z6), (-1/z6)
    ],
    [
        (-1/z6), (1/z2 + 1/z5 + 1/z6)
    ]
])

# Вектор свободных членов
B = np.array([
    ik - (e6 / z6) + (e3 / z4),
    (e6 / z6) - (e2 / z2) + (e3 / z5)
])

# Решение системы
try:
    phi = np.linalg.solve(A, B)
    print("Решение системы:")
    print(f"phi1 = {phi[0]}")
    print(f"phi2 = {phi[1]}")
    print(f"phi3 = {0}")  # phi3 задано
    print(f"phi4 = {e3}")  # phi4 задано
except np.linalg.LinAlgError:
    print("Система не имеет уникального решения.")
