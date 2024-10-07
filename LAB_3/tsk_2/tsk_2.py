import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os  # Импортируем модуль для работы с файловой системой

# URL с запросом "котики"
url = 'https://www.google.ru/search?q=котики'

async def google_session(): 
    # Создаем папку, если она не существует
    folder_name = "tsk_2"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)  # Создаем папку

    async with aiohttp.ClientSession() as session:  # создание асинхронной сессии
        async with session.get(url) as response:    # выполнение GET-запроса
            html = await response.text()           # получение содержимого ответа
            soup = BeautifulSoup(html, 'lxml')     # парсинг HTML с помощью BeautifulSoup
            
            # Сохраняем изменённый HTML в page.html
            with open(os.path.join(folder_name, "page.html"), "w", encoding="utf-8") as file:
                file.write(soup.prettify())        # сохраняем изменённый HTML с отступами

async def main():
    task = asyncio.create_task(google_session())  # создаем задачу
    await task                                    # ожидаем выполнения задачи

if __name__ == '__main__':
    asyncio.run(main())
    print(url)
