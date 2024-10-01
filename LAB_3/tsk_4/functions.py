import requests
import os

import requests
import os

# функция для поиска изображения через кастомную поисковую систему
def search_image_google(query):
    api_key = os.getenv('GOOGLE_API_KEY')  # API-ключ
    cx = os.getenv('GOOGLE_CX')  # ID Custom Search Engine (cx)
    search_url = "https://www.googleapis.com/customsearch/v1"
    
    params = {
        "q": query,  # запрос, по которому выполняется поиск
        "cx": cx,  # идентификатор поисковой системы
        "key": api_key,  # API-ключ
        "searchType": "image",  # указание на поиск изображения
        "num": 1,  # количество возвращаемых изображений 
    }
    
    response = requests.get(search_url, params=params) # ответ
    
    # логирование статуса и ответа от API
    print('Status code:', response.status_code)
    print('Response:', response.text) 
    
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            # возвращаем URL первой найденной картинки
            image_url = data["items"][0]["link"]
            return image_url
        else:
            print("Изображение не найдено.")
            return None
    else:
        print('Ошибка запроса:', response.status_code)
        return None
