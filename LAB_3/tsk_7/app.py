import random
import tkinter as tk
from tkinter import ttk 

from functions import *

def main():
    array_size = 10_000_000
    array = [random.randint(1, 100) for _ in range(array_size)]

    root = tk.Tk()
    root.title("Калькулятор суммы массива")

    # работа с виджетом 
    frame = ttk.Frame(root, padding="10") 
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="Выберите количество потоков (N):").grid(row=0, column=0, sticky=tk.W)

    N_values = [1, 2, 4, 8, 16]  # список допустимых значений для количества потоков.
    N_var = tk.IntVar(value=N_values[0])  # переменная для хранения выбранного значения из выпадающего списка

    # выпадающий список
    N_combobox = ttk.Combobox(frame, textvariable=N_var, values=N_values)  
    N_combobox.grid(row=0, column=1, sticky=tk.W)

    # надписи 
    result_label = ttk.Label(frame, text="")
    result_label.grid(row=1, column=0, columnspan=2, sticky=tk.W)

    def on_calculate():
        N = N_var.get()
        calculate_sum(N, array, result_label)

    calculate_button = ttk.Button(frame, text="Вычислить", command=on_calculate)
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()