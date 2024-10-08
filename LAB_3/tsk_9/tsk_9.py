import multiprocessing
import tkinter as tk
from tkinter import messagebox
import time  # Импортируем модуль time

# функция для выполнения работы в подпроцессах
def put_index(index):
    return f'item {index}'

# функция, запускающая несколько процессов и обрабатывающая их результаты
def run_processes():
    start_time = time.time()

    with multiprocessing.Pool(processes=5) as pool:
        results = pool.map(put_index, range(5))

    end_time = time.time()

    LIST = " ".join(results)  # объединение элементов списка в одну строку
    messagebox.showinfo("Результат", f"Список после выполнения процессов: {LIST}\nВремя выполнения: {end_time - start_time :.4f} секунд")

def main():
    root = tk.Tk()
    root.title("Многопроцессорное приложение")

    start_button = tk.Button(root, text="Запустить процессы", command=run_processes)
    start_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    multiprocessing.freeze_support()  # нужно для корректной работы multiprocessing на Windows
    main()  # запускаем только в главном процессе
