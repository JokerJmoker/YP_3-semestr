import multiprocessing
import tkinter as tk
from tkinter import messagebox
import time  # Импортируем модуль time

# функция для выполнения работы в подпроцессах
def put_index(index, LIST):
    LIST.append(f'item {index}')  # добавляем элемент в общий список

def run_processes_1(): 
    manager = multiprocessing.Manager()  # интерфейс для создания общих объектов 
    LIST = manager.list()

    processes = [
        multiprocessing.Process(target=put_index, args=(i, LIST))  # передаем индекс и список
        for i in range(5)  # например 5 процессов
    ]  

    start_time = time.time()  # Запоминаем время начала

    # запуск и ожидание завершения процессов
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    end_time = time.time()  # Запоминаем время окончания

    result = " ".join(LIST)  # объединение элементов списка в одну строку
    messagebox.showinfo("Результат", f"Список после выполнения процессов: {result}\nВремя выполнения: {end_time - start_time:.4f} секунд")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Многопроцессорное приложение")

    start_button = tk.Button(root, text="Запустить процессы", command=run_processes_1)
    start_button.pack(pady=20)

    root.mainloop()
