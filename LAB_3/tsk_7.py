import threading
import time
import random
import tkinter as tk
from tkinter import ttk  # импорт виджетов 

# функция для суммирования части массива
def sum_array_part(array, start, end, result):
    result.append(sum(array[start:end]))  # список для хранения суммы,

# функция для вычисления суммы с использованием N потоков 
def calculate_sum(N, array, result_label):
    start_time = time.time()

    threads = []
    results = []
    chunk_size = len(array) // N  # размер части массива, которую будет обрабатывать каждый поток.

    for i in range(N):
        # диапазон индексов массива
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < N - 1 else len(array)
        result = []
        thread = threading.Thread(target=sum_array_part, args=(array, start, end, result))
        threads.append(thread)
        results.append(result)
        thread.start()
    # ожидаем завершения всех потоков 
    for thread in threads:
        thread.join()

    total_sum = sum(sum(result) for result in results)
    end_time = time.time()

    result_label.config(text=f"N = {N}, Общая сумма: {total_sum}, Время выполнения: {end_time - start_time:.4f} секунд")


def main():
    array_size = 10000000
    array = [random.randint(1, 100) for _ in range(array_size)]

    root = tk.Tk()
    root.title("Калькулятор суммы массива")

    # работа с виджетом 
    frame = ttk.Frame(root, padding="10") 
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="Выберите количество потоков (N):").grid(row=0, column=0, sticky=tk.W)

    N_values = [1, 2, 4, 8, 16]  # список допустимых значений для количества потоков.
    N_var = tk.IntVar(value=N_values[0])  # переменная для хранения выбранного значения из выпадающего списка
    """
    выпадающий список - элемент графического пользовательского интерфейса (GUI), который позволяет пользователю 
    выбрать одно значение из заранее определенного набора опций
    """
    N_combobox = ttk.Combobox(frame, textvariable=N_var, values=N_values)  
    N_combobox.grid(row=0, column=1, sticky=tk.W)

    # надписи 
    result_label = ttk.Label(frame, text="")
    result_label.grid(row=1, column=0, columnspan=2, sticky=tk.W)

    # ...---...
    def on_calculate():
        N = N_var.get()
        calculate_sum(N, array, result_label)

    calculate_button = ttk.Button(frame, text="Вычислить", command=on_calculate)
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
