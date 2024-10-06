import aiohttp
from aiohttp import web
import asyncio

# функция для асинхронного HTTP-клиента
async def fetch_google():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://google.com') as resp:
            text = await resp.text()
            print('{:.70}...'.format(text))  # Печать первых 70 символов

# асинхронная функция-обработчик запросов для сервера
async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name
    # ...
    # здесь идет некоторая дополнительная логика с async/await
    return web.Response(text=text)

# основная функция для запуска сервера и клиента
async def main():
    # запуск HTTP-клиента
    await fetch_google()

    # настройка и запуск веб-сервера
    app = web.Application() # cоздает новый экземпляр приложения веб-сервера.
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)]) # Добавляет маршруты для обработки HTTP-запросов

    # запуск сервера
    runner = web.AppRunner(app) # управляет жизненным циклом приложения.
    await runner.setup() # Инициализирует AppRunner, чтобы он мог принимать запросы
    site = web.TCPSite(runner, 'localhost', 8080) # Создает TCP-сайт на локальном хосте, который слушает на порту 8080
    await site.start() # Запускает сервер, чтобы он начал принимать входящие запросы

    print("Server started at http://localhost:8080")

    # ожидание завершения сервера
    while True:
        await asyncio.sleep(3600)

# запуск программы
if __name__ == '__main__':
    asyncio.run(main())  
