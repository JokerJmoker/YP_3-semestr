import urllib.request
import threading
import time
import queue


urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]


def read_url(url):
    with urllib.request.urlopen(url) as url: # открываем соединение по указанному url,которое при помощи with закроестя при выходе из блока  
        return url.read()

    
def run_threads(urls):
    threads = [
        threading.Thread(target=read_url, args=(url,))  
        for url in urls # выбираем диапазон проверяемых ip
    ]
    for thread in threads:
        thread.start()  # каждый поток должен быть запущен
    for thread in threads:
        thread.join()  # дожидаемся исполнения всех потоков


start = time.time()
for url in urls:
    read_url(url)
print('время выполнения задачи без использования потоков' , time.time() - start)

start = time.time()
run_threads(urls)
print('время выполнения задачи c использованием потоков' , time.time() - start)

input("Нажмите Enter, чтобы выйти...")
