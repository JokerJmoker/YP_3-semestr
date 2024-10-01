import tkinter as tk
from tkinter import messagebox  # модуль для отображения всплывающих сообщений.
from collections import namedtuple  # функция для создания неизменяемых кортежей с именованными полями.
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

# определение структуры данных для сервисов 
Service = namedtuple('Service', ('name', 'url', 'ip_attr'))  # проименовываем поля

# ipify и ip-api возвращают IP-адрес в формате JSON.
SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

# асинхронная функция для запроса ip 
async def fetch_ip(service):
    async with aiohttp.ClientSession() as session:  # создаем асинхронную сессию
        async with session.get(service.url) as response:  # отправляем запрос
            data = await response.json()
            return data[service.ip_attr]  # возвращаем ip по атрибуту ip_attr

# асинхронная функция для управления задачами 
async def asynchronous():
    tasks = [asyncio.create_task(fetch_ip(service)) for service in SERVICES]

    done, pending = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)  # возвращает результаты, как только одна из задач завершится

    for task in done:  # обработка завершённых задач
        try:
            ip = task.result()
            return ip
        except Exception as exception:
            print("ошибка при извлечении IP: {}".format(exception))

    for task in pending:  # отмена ожидающих задач
        task.cancel()

# получаем ip и обновляем интерфейс 
def get_ip():
    try:
        ip = asyncio.run(asynchronous())
        ip_label.config(text="Ваш IP адрес: {}".format(ip))
    except Exception as exception:
        messagebox.showerror("Error", "ошибка при получении ip: {}".format(exception))


root = tk.Tk()
root.title("Определить IP адрес")

button = tk.Button(root, text="Узнать IP", command=get_ip)
button.pack(pady=10)

ip_label = tk.Label(root, text="", font=("TimesNewRoman", 14))
ip_label.pack(pady=10)

root.mainloop()
