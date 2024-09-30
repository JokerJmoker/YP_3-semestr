from aiogram import Bot, Dispatcher, types               # асинхронная библиотека для работы с Telegram Bot API (создание бота и обработка сообщений.)
import requests                              # библиотека для отправки HTTP-запросов.
from bs4 import BeautifulSoup                # библиотека для парсинга HTML и XML документов. (извлечения данных из веб-страниц)


# прокси и токен для подключения
PROXY_URL = 'socks5://193.233.84.104:1080'
secret_token = '7314059265:AAEJjXlcq6M-SDdO5pUQ8eoTvrW9rZmpweU'


# создание экземпляров соответсвующих классов: бота и обработчика событий
bot = Bot(token=secret_token, proxy=PROXY_URL)
dp = Dispatcher(bot)


# функция для поиска изображения через Яндекс Картинки
def search_image_yandex(query):                                         # query - запрос
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }                                                                   # иммитация запроса от браузера во избежание блокировки 
    search_url = 'https://yandex.ru/images/search?text=' + {query}      # адрес для поиска изображений 
    response = requests.get(search_url, headers=headers)                # отправка get запроса на url
    soup = BeautifulSoup(response.content, 'html.parser')               # парсинг HTML-кода страницы с результатами поиска    
# поиск URL изображения
    images = soup.find_all('img', class_='serp-item__thumb')            # поиск всех тегов img с классом serp-item__thumb
    if images:
        image_url = 'https:' + images[0]['src']                         # берет первую найденную картинку из источник source 
        return image_url
    return None


# декоратор, который определяет функцию-обработчик для команд /start и /help.
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Шалом! Я ищи картиники по вашему запросу. Таки что найти?')


# декоратор для обработки всех входящих текстовых сообщений
@dp.message_handler()
# функция поиска картинок по полученным сообщениям 
async def send_image(message: types.Message):                           
    search_query = message.text
    image_url = search_image_yandex(search_query)
    
    if image_url:
        await message.reply_photo(image_url)                            # отправляем найденное изображение
    else:
        await message.reply("Извините, не удалось найти изображение.")


if __name__ == '__main__':
    dp.start_polling(bot)