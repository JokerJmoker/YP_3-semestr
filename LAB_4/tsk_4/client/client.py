import socket
import threading
import easygui
from encode import caesar_encrypt  # Импортируем функцию шифрования

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
            choice = easygui.buttonbox("Выберите действие", choices=["Шифровать и отправить", "Отправить зашифрованное сообщение", "Выход"])
            
            if choice == "Выход":
                break

            if choice == "Шифровать и отправить":
                file_path = easygui.fileopenbox("Выберите файл для отправки", title="Выбор файла")
                if file_path is None:
                    continue  
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        file_content = file.read()
                except Exception as e:
                    easygui.msgbox(f"Ошибка при чтении файла: {e}", title="Ошибка")
                    continue
                
                # Запрашиваем ключ для шифрования
                shift = easygui.enterbox("Введите ключ (сдвиг):", title="Ключ шифрования")
                if shift is None or not shift.isdigit():
                    easygui.msgbox("Ключ должен быть числом.", title="Ошибка")
                    continue

                shift = int(shift)
                encrypted_content = caesar_encrypt(file_content, shift)  # Шифруем содержимое файла
                
                # Отправляем зашифрованное содержимое файла на сервер
                client.send(encrypted_content.encode('utf-8'))  # Отправляем зашифрованный файл
                client.send(f"{shift}".encode('utf-8'))  # отправляем ключ

                # Печатаем зашифрованный текст в терминале
                print("Зашифрованный текст:")
                print(encrypted_content)

            elif choice == "Отправить зашифрованное сообщение":
                encrypted_file_path = easygui.fileopenbox("Выберите файл с зашифрованным сообщением", title="Выбор зашифрованного файла")
                if encrypted_file_path is None:
                    continue
                
                try:
                    with open(encrypted_file_path, 'r', encoding='utf-8') as file:
                        encrypted_content = file.read()
                except Exception as e:
                    easygui.msgbox(f"Ошибка при чтении файла: {e}", title="Ошибка")
                    continue
                
                # Запрашиваем ключ для расшифровки
                shift = easygui.enterbox("Введите ключ (сдвиг) для расшифровки:", title="Ключ расшифровки")
                if shift is None or not shift.isdigit():
                    easygui.msgbox("Ключ должен быть числом.", title="Ошибка")
                    continue

                shift = int(shift)

                # Отправляем зашифрованное сообщение на сервер
                client.send(encrypted_content.encode('utf-8'))  # Отправляем зашифрованный файл
                client.send(f"{shift}".encode('utf-8'))  # отправляем ключ

                print("Отправлено зашифрованное сообщение:")
                print(encrypted_content)

    except ConnectionRefusedError:
        easygui.msgbox("Не удалось подключиться к серверу. Убедитесь, что сервер запущен.", title="Ошибка подключения")
    except Exception as e:
        easygui.msgbox(f"Произошла ошибка: {e}", title="Ошибка")
    
    finally:
        client.close()  # закрываем сокет при завершении работы

if __name__ == "__main__":
    main()
