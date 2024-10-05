import multiprocessing
import tkinter as tk
from tkinter import messagebox


# функция для дальнейшей передачи списка list в подпроцессы 
def worker(list):
    list.append('item')

#  функция, запускающая несколько процессов и обрабатывающая их результаты.
def run_processes():
    manager = multiprocessing.Manager()  # интерфейс для создания общих объектов 
    LIST = manager.list()

    processes = [
        multiprocessing.Process(target=worker, args=(LIST,))
        for _ in range(5)
    ]  # например 5 процессов 
    # запуск и ожидание завершения процессов
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    result = " ".join(LIST)  # объединение элементов списка в одну строку, при разделении их пробелами.
    messagebox.showinfo("Результат", "Список после выполнения процессов: {}".format(result))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Многопроцессорное приложение")

    # Создаем кнопку для запуска процессов
    start_button = tk.Button(root, text="Запустить процессы", command=run_processes)
    start_button.pack(pady=20)

    root.mainloop()
