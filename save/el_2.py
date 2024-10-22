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
"""coeff_matrix = np.array([
    [z2 + z1 + z6, z6 + z2, z6],
    [z2 + z6, z6 + z2 + z4, z6 + z4],
    [z6, z6 + z4, z6 + z5 + z4]
])
"""
coeff_matrix = np.array([
    [1,0,0],
    [z2 + z6, z6 + z2 + z4, z6 + z4],
    [z6, z6 + z4, z6 + z5 + z4]
])
# Вектор свободных членов (B)
const_terms = np.array([ik, e6 + e2 + e3, e6])

# Решаем систему
solution = solve_linear_equations(coeff_matrix, const_terms)

# Вывод решения
if isinstance(solution, str):
    print(solution)
else:
    print("Решение системы уравнений:")
    print(f"i1 = {solution[0]:.4f}")
    print(f"i2 = {solution[1]:.4f}")
    print(f"i3 = {solution[2]:.4f}")
