import requests
from bs4 import BeautifulSoup

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