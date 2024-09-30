import os, re
import threading


received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

def thread_job(suffix): # определяем работу,передающуюся потоку
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


def run_threads(first_ip,last_ip):
    threads = [
        threading.Thread(target=thread_job, args=(i,)) # кортеж , 
        for i in range (first_ip,last_ip) # выбираем диапазон проверяемых ip
    ]
    for thread in threads:
        thread.start()  # каждый поток должен быть запущен
    for thread in threads:
        thread.join()  # дожидаемся исполнения всех потоков

def apply_ineffective_solution():
    for suffix in range(20, 30):
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


run_threads(20,30)
print('\n')
apply_ineffective_solution()
