import socket
import threading

clients = []  # список клиентов для рассылки сообщений



def handle_client(conn, addr):
    print(f"Новый клиент подключен: {addr}")
    clients.append(conn)
    
    while True:
        try:  # прием данных от клиента
            message = conn.recv(1024)
            if not message:
                break
            print(f"Получено сообщение от {addr}: {message.decode('utf-8')}")
            broadcast(message, conn)  # рассылка сообщений клиентам
        except:
            break
    
    conn.close()
    clients.remove(conn)
    print(f"Клиент отключился: {addr}")

# отправка сообщений 
def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def command_listener(server):
    while True:
        command = input()
        if command.lower() == 'exit':
            print("Сервер остановлен.")
            server.close()  # закрываем серверный сокет
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 55000))
    server.listen(5)
    print("Сервер запущен, ожидаем подключения клиентов...")

    thread = threading.Thread(target=command_listener, args=(server,), daemon=True)
    thread.start()

    try:
        while True:
            conn, addr = server.accept()  # новое соединение
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()  # новый поток для клиента

            # Обработка команды в консоли
            command = input()
            if command.lower() == 'exit':
                break  # выход из цикла, если введена команда "exit"
    except KeyboardInterrupt:
        print("Сервер остановлен.")
    finally:
        server.close()  # закрываем серверный сокет

if __name__ == "__main__":
    main()
