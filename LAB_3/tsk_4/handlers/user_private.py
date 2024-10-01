# работа с очередью сообщений

from aiogram import types, Router
from aiogram.filters import Command
from functions import search_image_google

user_private_router = Router()

# декоратор, который определяет функцию-обработчик для команд /start 
@user_private_router.message(Command("start"))
async def send_welcome(message: types.Message): # для подсказок при написании 
    await message.reply('Шалом! Я могу найти картинку по запросу. Таки что мы ищем?')


# декоратор для обработки всех входящих текстовых сообщений
@user_private_router.message()
async def send_image(message: types.Message):
    search_query = message.text
    image_url = search_image_google(search_query)

    if image_url:
        await message.reply_photo(image_url)  # Отправляем найденное изображение
    else:
        await message.reply("Извините, не удалось найти изображение.")