# стандартные модули
import asyncio
import os                                                                   # Делать нормально, чтобы было нормально

# фреймворк
from aiogram import Bot, Dispatcher

# подргрузка переменных окружения
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

# импорты проекта 
from handlers.user_private import user_private_router
ALLOWED_UPDATES = ['message, edited_message']


# ТГ общается с ботом при помощи словарей

# Создание экземпляров классов: бота и диспетчера
bot = Bot(token=os.getenv('TOKEN'), proxy=os.getenv('PROXY_URL'))
dp = Dispatcher()

dp.include_router(user_private_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True) # пропуск обновлений, пока бот был оффлайн
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == '__main__':
    asyncio.run(main())
