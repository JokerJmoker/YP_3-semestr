import socket
import threading

clients = []  # список клиентов для рассылки сообщений
server_running = True  # флаг для остановки сервера


def handle_client(conn, addr):
    print(f"Новый клиент подключен: {addr}")
    clients.append(conn)

    while server_running:  # продолжаем, пока сервер работает
        try:
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


def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)


def command_listener(server):
    global server_running
    while server_running:
        command = input()
        if command.lower() == 'exit':
            print("Сервер остановлен.")
            server_running = False
            server.close()  # закрываем серверный сокет
            break


def main():
    global server_running
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 55000))
    server.listen(5)
    print("Сервер запущен, ожидаем подключения клиентов...")
    print("Чтобы отключить сервер, введите exit")
    thread = threading.Thread(target=command_listener, args=(server,), daemon=True)
    thread.start()

    try:
        while server_running:
            try:
                conn, addr = server.accept()  # новое соединение
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()  # новый поток для клиента
            except OSError:
                break  # сервер был закрыт, выходим из цикла
    except KeyboardInterrupt:
        print("Сервер остановлен через KeyboardInterrupt.")
    finally:
        # Закрываем все активные соединения перед завершением
        for client in clients:
            client.close()
        server.close()  # закрываем серверный сокет


if __name__ == "__main__":
    main()
