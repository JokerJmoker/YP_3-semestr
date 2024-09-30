from aiogram import types, Router
from aiogram.filters import Command
from functions import search_image_yandex

user_private_router = Router()

# Первая очередность размещения 
@user_private_router.message(Command("start")) # декоратор обработки событий. Установки фильтра start
async def send_welcome(message: types.Message):
    await message.reply('Шалом! Я ищу картинки по вашему запросу. Что найти?')

@user_private_router.message()
async def send_image(message: types.Message):
    search_query = message.text
    image_url = search_image_yandex(search_query)

    if image_url:
        await message.reply_photo(image_url) # можно и answer. reply - ответ
    else:
        await message.reply("Извините, не удалось найти изображение.")
