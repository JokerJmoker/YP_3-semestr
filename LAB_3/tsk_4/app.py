# стандартные модули
import asyncio
import os

# фреймворк
from aiogram import Bot, Dispatcher

# подгрузка переменных окружения
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

# импорты проекта 
from handlers.user_private import user_private_router
ALLOWED_UPDATES = ['message', 'edited_message']

# Создание экземпляров классов: бота и диспетчера
bot = Bot(token=os.getenv('TOKEN'), proxy=os.getenv('PROXY_URL'))
dp = Dispatcher()

dp.include_router(user_private_router)

async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True) # пропуск обновлений, пока бот был оффлайн
        print("Bot webhook deleted successfully.")
        await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(main())