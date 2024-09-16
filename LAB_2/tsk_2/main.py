from tsks import *  # Импортируйте только необходимую функцию

if __name__ == '__main__':
    print("Выберите задание:")
    task = int(input())
    
    if task == 2:
        tsk_2_2.tsk_2_2()
    if input() == 3:
        tsk_2_3()
    if input() == 4:
        tsk_2_4()
    if input() == 5:
        tsk_2_5()
    if input() == 6:
        tsk_2_6()
    if input() == 7:
        tsk_2_7()
    else:
        print("Неверный выбор задания.")