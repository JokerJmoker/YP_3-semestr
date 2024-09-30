from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import requests
from bs4 import BeautifulSoup
import asyncio

# ТГ общается с ботом при помощи словарей

# Прокси и токен для подключения
PROXY_URL = 'socks5://193.233.84.104:1080'
TOKEN = '7314059265:AAEJjXlcq6M-SDdO5pUQ8eoTvrW9rZmpweU'  # Замените на ваш токен

# Создание экземпляров классов: бота и диспетчера
bot = Bot(token=TOKEN, proxy=PROXY_URL)
dp = Dispatcher()

# Функция для поиска изображения через Яндекс Картинки
def search_image_yandex(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    search_url = f'https://yandex.ru/images/search?text={query}'  # Формирование URL
    response = requests.get(search_url, headers=headers)

    # Проверяем, что запрос выполнен успешно
    if response.status_code != 200:
        print(f"Ошибка при запросе к Яндекс: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')

    # Проверяем все изображения и ищем корректный URL
    for img in images:
        img_src = img.get('src')
        if img_src and img_src.startswith('https://'):
            return img_src

    return None

# Первая очередность размещения 
@dp.message(Command("start")) # декоратор обработки событий. Установки фильтра start
async def send_welcome(message: types.Message):
    await message.reply('Шалом! Я ищу картинки по вашему запросу. Что найти?')

@dp.message()
async def send_image(message: types.Message):
    search_query = message.text
    image_url = search_image_yandex(search_query)

    if image_url:
        await message.reply_photo(image_url) # можно и answer. reply - ответ
    else:
        await message.reply("Извините, не удалось найти изображение.")

# Запуск бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True) # пропуск обновлений, пока бот был оффлайн
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
