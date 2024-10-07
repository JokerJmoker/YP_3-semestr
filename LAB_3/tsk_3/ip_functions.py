import asyncio
from concurrent.futures import FIRST_COMPLETED
from collections import namedtuple
import aiohttp
import time  # модуль для работы со временем

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
async def asynchronous(log):
    start_time = time.time()  # фиксируем время начала
    tasks = []
    for service in SERVICES:
        task = asyncio.create_task(fetch_ip(service))
        tasks.append(task)
        log(f"Задача для {service.name} поставлена.")

    done = None
    pending = None

    wait_result = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)
    done = wait_result[0]  # набор завершенных задач
    pending = wait_result[1]  # набор ожидающих задач

    for task in done:  # обработка завершённых задач
        try:
            ip = task.result()
            log(f"Задача {service.name} завершилась первой")
            end_time = time.time()  # фиксируем время завершения
            log(f"Время выполнения: {end_time - start_time:.2f} секунд")
            return ip
        except Exception as exception:
            log(f"Ошибка при извлечении IP: {format(exception)}")

    for task in pending:  # отмена ожидающих задач
        task.cancel()