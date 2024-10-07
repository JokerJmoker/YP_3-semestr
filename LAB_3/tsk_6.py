import os
import re
import threading
import time  # Импортируем модуль для работы со временем

received_packages = re.compile(r"(\d) received")  # объект регулярного выражения
status = ("no response", "alive but losses", "alive")

def thread_job(suffix):  # определяем работу, передающуюся потоку
    ip = "192.168.178." + str(suffix)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта 
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])

def run_threads(first_ip, last_ip):
    threads = [
        threading.Thread(target=thread_job, args=(i,)) 
        for i in range(first_ip, last_ip)  # выбираем диапазон проверяемых ip
    ]
    for thread in threads:
        thread.start()  # каждый поток должен быть запущен
    for thread in threads:
        thread.join()  # дожидаемся исполнения всех потоков

def apply_ineffective_solution(first_ip, last_ip):
    for suffix in range(first_ip, last_ip):
        ip = "192.168.178." + str(suffix)
        ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
        print("... pinging ", ip)
        while True:
            line = ping_out.readline()
            if not line:
                break
            n_received = received_packages.findall(line)
            if n_received:
                print(ip + ": " + status[int(n_received[0])])

first_ip = 20
last_ip = 30

# Дублирование кода -_-

start_time = time.time()  
run_threads(first_ip, last_ip)
end_time = time.time()  
print(f"Время выполнения программы при помощи потоков: {end_time - start_time:.2f} секунд\n")

start_time = time.time()  
apply_ineffective_solution(first_ip, last_ip)
end_time = time.time()  
print(f"Время выполнения программы без помощи потоков: {end_time - start_time:.2f} секунд\n")

input("Нажмите Enter, чтобы выйти...")
