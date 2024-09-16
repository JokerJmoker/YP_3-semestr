from tsks import *  # Импортируйте только необходимую функцию

if __name__ == '__main__':
    print("Выберите задание:")
    task = int(input())
    
    if task == 2:
        tsk_2_2.tsk_2_2()
    elif task == 3:
        tsk_2_3.tsk_2_3()
    elif task == 4:
        tsk_2_4.tsk_2_4()
    elif task == 5:
        tsk_2_5.tsk_2_5()
    elif task == 6:
        tsk_2_6.tsk_2_6()
    elif task == 7:
        tsk_2_7.tsk_2_7()
    else:
        print("Неверный выбор задания.")