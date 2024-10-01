import requests
from bs4 import BeautifulSoup
import aiohttp
import os

# Функция для поиска изображения через Яндекс Картинки
def search_image_google(query):
    api_key = os.getenv('GOOGLE_API_KEY')  # Твой API-ключ
    cx = os.getenv('GOOGLE_CX')  # Твой ID Custom Search Engine (cx)
    search_url = "https://www.googleapis.com/customsearch/v1"
    
    params = {
        "q": query,  # Запрос, по которому выполняется поиск
        "cx": cx,  # Идентификатор поисковой системы
        "key": api_key,  # API-ключ
        "searchType": "image",  # Указываем, что хотим искать изображения
        "num": 1,  # Количество возвращаемых изображений (в нашем случае — одно)
    }
    
    response = requests.get(search_url, params=params)
    
    # Логирование статуса и ответа от API
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            # Возвращаем URL первой найденной картинки
            image_url = data["items"][0]["link"]
            return image_url
        else:
            print("Изображение не найдено.")
            return None
    else:
        print(f"Ошибка запроса: {response.status_code}")
        return None