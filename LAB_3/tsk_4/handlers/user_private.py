from aiogram import types, Router
from aiogram.filters import Command
from functions import search_image_google

user_private_router = Router()

@user_private_router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply('Привет! Я могу найти картинку по запросу. Что найти?')

@user_private_router.message()
async def send_image(message: types.Message):
    search_query = message.text
    image_url = search_image_google(search_query)

    if image_url:
        await message.reply_photo(image_url)  # Отправляем найденное изображение
    else:
        await message.reply("Извините, не удалось найти изображение.")