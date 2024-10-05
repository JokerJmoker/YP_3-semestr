import threading
import random
import time
import sys


def thread_job():
    with lock: # контекстный менеджером  + эксклюзивный доступ 
        global counter
        old_counter = counter
        time.sleep(random.randint(0, 1))
        counter = old_counter + 1
        print('{} '.format(counter), end='')
        sys.stdout.flush()


lock = threading.Lock() # Создает объект блокировки lock, который используется для синхронизации потоков.
counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print('\n', counter)
