import aiohttp
from aiohttp import web
import asyncio

async def google_session():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://google.com') as resp:
            text = await resp.text()
            print('{:.70}...'.format(text))

async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name
    # ...
    # здесь идет некоторая дополнительная логика с async/await
    #await google_session()
    #
    return web.Response(text=text) 
     
async def main():
    # Запуск HTTP-клиента
    await google_session()

    # Настройка и запуск веб-сервера
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])


    print("Server started at http://localhost:8080")

    
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())