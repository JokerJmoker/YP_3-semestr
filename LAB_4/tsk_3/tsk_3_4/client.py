import socket
import threading
import easygui

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024)
            if not message:
                break
            easygui.msgbox(message.decode('utf-8'), title="Результат от сервера")
        except Exception as e:
            easygui.msgbox(f"Ошибка при получении сообщения: {e}", title="Ошибка")
            break

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 55000))  # подключаемся к серверу
        
        # запускаем поток для получения сообщений
        threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
        
        while True:
            # Предлагаем выбор: отправить сообщение или файл
            choice = easygui.buttonbox("Выберите действие:", title="Выбор действия", 
                                       choices=["Отправить сообщение", "Отправить файл", "Выход"])
            
            if choice == "Отправить сообщение":
                # Ввод сообщения
                message = easygui.enterbox("Введите сообщение:", title="Чат клиент")
                if message is None or message.lower() == 'exit':
                    break
                client.send(message.encode('utf-8'))  # отправляем сообщение на сервер

            elif choice == "Отправить файл":
                # Запрашиваем файл у пользователя
                file_path = easygui.fileopenbox("Выберите файл для отправки", title="Выбор файла")
                if file_path is None:
                    continue
                
                # Читаем содержимое файла
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        file_content = file.read()
                except Exception as e:
                    easygui.msgbox(f"Ошибка при чтении файла: {e}", title="Ошибка")
                    continue
                
                # Отправляем содержимое файла на сервер
                client.send(file_content.encode('utf-8'))
            
            elif choice == "Выход":
                break
    
    except ConnectionRefusedError:
        easygui.msgbox("Не удалось подключиться к серверу. Убедитесь, что сервер запущен.", title="Ошибка подключения")
    except Exception as e:
        easygui.msgbox(f"Произошла ошибка: {e}", title="Ошибка")
    
    finally:
        client.close()  # закрываем сокет при завершении работы

if __name__ == "__main__":
    main()
