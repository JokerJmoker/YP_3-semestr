import aiohttp
from aiohttp import web
import asyncio

async def google_session(): # 
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.google.ru/?hl=ru') as resp:
            text = await resp.text()
            print('{:.70}...'.format(text))

async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name
    # ...
    # здесь идет некоторая дополнительная логика с async/await
    await google_session()
    #
    return web.Response(text=text) 
     
if __name__ == '__main__':
    # настройка сервера
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])

    web.run_app(app)
