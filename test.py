from tsk_1 import *

numbers = input_numbers()

# Глобальные переменные для количества итераций
iterations_counter = 0

# сортировка пузырьками
def bubble_sort(numbers_list):
    global iterations_counter
    iterations_counter = 0  # Сброс счётчика итераций
    flag = True
    while flag:
        flag = False
        for i in range(len(numbers_list) - 1):
            iterations_counter += 1
            if numbers_list[i] > numbers_list[i + 1]:
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]
                flag = True

# сортировка вставками
def insertion_sort(numbers_list):  
    global iterations_counter
    iterations_counter = 0  # Сброс счётчика итераций
    for i in range(1, len(numbers_list)):
        item = numbers_list[i]
        i2 = i - 1
        while i2 >= 0 and numbers_list[i2] > item:
            iterations_counter += 1
            numbers_list[i2 + 1] = numbers_list[i2]
            i2 -= 1
        numbers_list[i2 + 1] = item
        iterations_counter += 1

# сортировка слиянием
def merge_sort(sort_nums):
    global iterations_counter
    iterations_counter = 0  # Сброс счётчика итераций

    def merge_sort_helper(sort_nums):
        global iterations_counter
        if len(sort_nums) > 1:
            mid = len(sort_nums) // 2
            lefthalf = sort_nums[:mid]
            righthalf = sort_nums[mid:]
            merge_sort_helper(lefthalf)
            merge_sort_helper(righthalf)
            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                iterations_counter += 1
                if lefthalf[i] < righthalf[j]:
                    sort_nums[k] = lefthalf[i]
                    i += 1
                else:
                    sort_nums[k] = righthalf[j]
                    j += 1
                k += 1
            while i < len(lefthalf):
                iterations_counter += 1
                sort_nums[k] = lefthalf[i]
                i += 1
                k += 1
            while j < len(righthalf):
                iterations_counter += 1
                sort_nums[k] = righthalf[j]
                j += 1
                k += 1

    merge_sort_helper(sort_nums)

# быстрая сортировка
def partition(sort_nums, begin, end):
    global iterations_counter
    iterations_counter = 0  # Сброс счётчика итераций
    part = begin
    for i in range(begin + 1, end + 1):
        iterations_counter += 1
        if sort_nums[i] <= sort_nums[begin]:
            part += 1
            sort_nums[i], sort_nums[part] = sort_nums[part], sort_nums[i]
    sort_nums[part], sort_nums[begin] = sort_nums[begin], sort_nums[part]
    return part

def quick_sort(sort_nums, begin=0, end=None):
    global iterations_counter
    if end is None:
        end = len(sort_nums) - 1
    
    def quick(sort_nums, begin, end):
        if begin >= end:
            return
        part = partition(sort_nums, begin, end)
        quick(sort_nums, begin, part - 1)
        quick(sort_nums, part + 1, end)

    quick(sort_nums, begin, end)

choose = input("Выберите метод сортировки \n сортировка пузырьками - a\n сортировка вставками - b\n сортировка слиянием - c\n быстрая сортировка - d\n")
print("Изначальный список:", numbers)

if choose == "a":
    bubble_sort(numbers)
elif choose == "b":
    insertion_sort(numbers)
elif choose == "c":
    merge_sort(numbers)
elif choose == "d":
    quick_sort(numbers)

print("Отсортированный список:", numbers)
print("Количество итераций:", iterations_counter)
