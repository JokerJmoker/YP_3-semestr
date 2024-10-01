import os
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()

# Проверка значений переменных окружения
api_key = os.getenv('GOOGLE_API_KEY')
cx = os.getenv('GOOGLE_CX')
token = os.getenv('TOKEN')
proxy_url = os.getenv('PROXY_URL')

print(f"API Key: {api_key}, CX: {cx}, TOKEN: {token}, PROXY: {proxy_url}")
