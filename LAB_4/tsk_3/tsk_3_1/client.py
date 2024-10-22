import socket 
import threading 
 
def receive_messages(sock): 
    while True: 
        try: 
            message = sock.recv(1024) 
            if not message: 
                break 
            print(f"Сообщение от сервера: {message.decode('utf-8')}") 
        except: 
            print("Ошибка при получении сообщения.") 
            break 
 
def main(): 
    try: 
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        client.connect(('localhost', 55000))  # подключаемся к серверу 
 
        # запускаем поток для получения сообщений 
        threading.Thread(target=receive_messages, args=(client,), daemon=True).start() 
 
        while True: 
            message = input("Введите сообщение: ") 
            if message.lower() == 'exit': 
                break 
            client.send(message.encode('utf-8'))  # Отправляем сообщение на сервер 
 
    except ConnectionRefusedError: 
        print("Не удалось подключиться к серверу. Убедитесь, что сервер запущен.") 
    except Exception as e: 
        print(f"Произошла ошибка: {e}") 
 
    client.close() 
 
if __name__ == "__main__": 
    main()