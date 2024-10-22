# Заданные комплексные числа
i1 = -3 + 1j
i2 = -2 - 3j
i3 = -5
i4 = 3 - 3j
i5 = -2j

z1 = -40j
z2 = 30j
z4 = 20 + 90j
z5 = 70 - 20j
z6 = -20j

# Вычисление u
u1 = i1 * z4
u2 = i2 * z6
u3 = i3 * z2
u4 = i4 * z5
u5 = i5 * 0 

# Вычисление модулей
mod_u1 = abs(u1)
mod_u2 = abs(u2)
mod_u3 = abs(u3)
mod_u4 = abs(u4)
mod_u5 = abs(u5)

# Красивый вывод модулей
print("Модули комплексных чисел u:")
print(f"|u1| = {mod_u1:.2f}")
print(f"|u2| = {mod_u2:.2f}")
print(f"|u3| = {mod_u3:.2f}")
print(f"|u4| = {mod_u4:.2f}")
print(f"|u5| = {mod_u5:.2f}")
