#Создать список чисел меньших 2500, оканчивающихся на 1 и являющихся квадратами целых чисел.
numbers = []
for i in range(1, 2500):
    number = i**2
    if str(number)[-1] == '1' and number < 2500 :
        numbers.append(number)  
print(numbers)