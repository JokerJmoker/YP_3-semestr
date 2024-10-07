import tkinter as tk
from tkinter import messagebox  # модуль для отображения всплывающих сообщений.
from ip_functions import asynchronous  # импортируем асинхронную функцию
import asyncio

# лог-функция для вывода сообщений в текстовое окно
def log(message):
    log_text.insert(tk.END, message + "\n")  # добавляем сообщение с переносом строки
    log_text.see(tk.END)  # прокрутка к последнему сообщению

# получаем ip и обновляем интерфейс 
def get_ip():
    try:
        ip = asyncio.run(asynchronous(log))
        ip_label.config(text="Ваш IP адрес: {}".format(ip))
    except Exception as exception:
        messagebox.showerror("Error", "Ошибка при получении ip: {}".format(exception))

# приложение 
root = tk.Tk()
root.title("Определить IP адрес")

# добавляем кнопку
button = tk.Button(root, text="Узнать IP", command=get_ip)
button.pack(pady=10)

# добавляем метку для IP
ip_label = tk.Label(root, text="", font=("TimesNewRoman", 14))
ip_label.pack(pady=10)

# добавляем текстовый виджет для вывода сообщений
log_text = tk.Text(root, height=10, width=50)
log_text.pack(pady=10)

root.mainloop()