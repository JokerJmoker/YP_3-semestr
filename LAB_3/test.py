import aiohttp
from aiohttp import web
import asyncio

# Функция для асинхронного HTTP-клиента
async def fetch_google():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://google.com') as resp:
            text = await resp.text()
            print('{:.70}...'.format(text))  # Печать первых 70 символов

# Асинхронная функция-обработчик запросов для сервера
async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name
    return web.Response(text=text)

# Основная функция для запуска сервера и клиента
async def main():
    # Запуск HTTP-клиента
    await fetch_google()

    # Настройка и запуск веб-сервера
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    print("Server started at http://localhost:8080")

    # Ожидание завершения сервера
    while True:
        await asyncio.sleep(3600)

# Запуск программы
if __name__ == '__main__':
    asyncio.run(main())  
