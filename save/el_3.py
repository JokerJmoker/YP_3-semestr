import numpy as np

def solve_linear_equations(coeff_matrix, const_terms):
    try:
        # Решаем систему линейных уравнений
        solution = np.linalg.solve(coeff_matrix, const_terms)
        return solution
    except np.linalg.LinAlgError:
        return "Система не имеет решений или имеет бесконечно много решений."

# Пример: Решение системы 4x4
# Система уравнений:
ik = -5 -2j
e2 = -550 + 320j
e3 = 400 - 200j
e6 = 240 + 20j


z1 = -40j
z2 = 30j
z4 = 20 + 90j
z5 = 70 - 20j
z6 = -20j

# Матрица коэффициентов (A)
coeff_matrix = np.array([
    [1/z1 + 1/z4 + 1/z6, -1/z6 ,0 , -1/z4 ],
    [-1/z6, 1/z2+1/z5+1/z6 , 0 , -1/z5 ],
    [0,0,1,0],
    [0,0,0,1]
])

# Вектор свободных членов (B)
const_terms = np.array([ik-e6/z6,e6/z6-e2/z2,0,e3])

# Решаем систему
solution = solve_linear_equations(coeff_matrix, const_terms)

# Вывод решения
if isinstance(solution, str):
    print(solution)
else:
    print("Решение системы уравнений:")
    print(f"phi_1 = {solution[0]:.3f}")
    print(f"phi_2 = {solution[1]:.3f}")
    print(f"phi_3 = {solution[2]:.3f}")
    print(f"phi_4 = {solution[3]:.3f}")

    phi_1 = solution[0]
    phi_2 = solution[1]
    phi_3 = solution[2]
    phi_4 = solution[3]

# Комплексные значения для i1, i2, i3, i4
i1 = (phi_1 - phi_4) / z4
i2 = (phi_1 - phi_2) / z6
i3 = (phi_2 - phi_3 +e2) / z2
i4 = (phi_2 - phi_4) / z5

# Вывод значений с округлением до 3 знаков после запятой
print(f"i1: {i1:.3f}")
print(f"i2: {i2:.3f}")
print(f"i3: {i3:.3f}")
print(f"i4: {i4:.3f}")
