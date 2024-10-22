import socket
import threading

clients = []  # список клиентов для рассылки сообщений
server_running = True  # флаг для остановки сервера


def handle_client(conn, addr):
    print(f"Новый клиент подключен: {addr}")
    clients.append(conn)

    while server_running:  # продолжаем, пока сервер работает
        try:
            # прием данных от клиента
            data = conn.recv(4096)  # увеличиваем буфер для больших файлов
            if not data:
                break
            
            file_content = data.decode('utf-8')
            print(f"Получен файл от {addr}, содержимое:\n{file_content}")
            
            # Подсчитываем количество слов
            word_count = len(file_content.split())
            response = f"Количество слов в файле: {word_count}"
            
            # Отправляем результат обратно клиенту
            conn.send(response.encode('utf-8'))
        
        except Exception as e:
            print(f"Ошибка при обработке клиента {addr}: {e}")
            break

    conn.close()
    clients.remove(conn)
    print(f"Клиент отключился: {addr}")


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
        for client in clients:
            client.close()
        server.close()  # закрываем серверный сокет


if __name__ == "__main__":
    main()
