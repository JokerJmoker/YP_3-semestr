"""
Написать программу поиска максимума, минимума, среднего значения и среднеквадратичного отклонения в последовательности. 
Числа задаются построчно. Окончание последовательности — слово End.
"""

import math

def input_numbers():
    numbers = []
    print("Введите число или End \n")
    while True:
        input_sth = input()
        if input_sth.lower() == "end": # нивелируем значение регистра
            break
        try:
            number = float(input_sth)  # Преобразует введенные числа к типу float
            numbers.append(number)
        except ValueError:
            print("Пожалуйста, введите число или 'End'")
    return numbers  


numbers = input_numbers()
if len(numbers) > 0:
    maximum = max(numbers)
    minimum = min(numbers)
    average_value = sum(numbers) / len(numbers)
    standard_deviation = math.sqrt(sum((x - average_value) ** 2 for x in numbers) / len(numbers))
    
    # Вывод результатов с использованием f-strings
    print("Максимум: ", maximum)
    print("Минимум: ", minimum)
    print(f"Среднее: {average_value:.2f}")
    print(f"Среднеквадратичное отклонение: {standard_deviation:.2f}")
else:
    print("Последовательность пуста.")
