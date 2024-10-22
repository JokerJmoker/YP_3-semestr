import os
from classes import Tree  

def main():
    tree = Tree()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    backup_file = os.path.join(current_directory, 'tree_backup.pkl')
    
 
    tree.show_commands()
    
    while True:
        command = input("Введите команду: ").strip().split() # убираем пробелы и разбиваем строку список слов
        
        if len(command) == 0: # проверка на пустую команду - список команд пустой 
            continue
        
        cmd = command[0] # извлечение первого слова из списка - т.е команды 
        
        if cmd == "add":
            if len(command) > 1: # проверка наличия аргументов ["command",[arg]]
                try:
                    tree.add(int(command[1])) # работаем только с int 
                except ValueError:
                    print("Ошибка: Необходимо ввести целое число.")
            else:
                print("Ошибка: Необходимо указать число.")
        # по аналогии 
        elif cmd == "find":
            if len(command) > 1:
                try:
                    found, level, direction = tree.find(int(command[1]))
                    if found:
                        print(f"Найдено на уровне {level}. Направление: {direction}.")
                    else:
                        print("Не найдено.")
                except ValueError:
                    print("Ошибка: Необходимо ввести целое число.")
            else:
                print("Ошибка: Необходимо указать число.")
        
        elif cmd == "delete":
            if len(command) > 1:
                try:
                    tree.delete(int(command[1]))
                except ValueError:
                    print("Ошибка: Необходимо ввести целое число.")
            else:
                print("Ошибка: Необходимо указать число.")
        
        elif cmd == "print":
            tree.print_tree()
        
        elif cmd == "clear":
            tree.clear()
            print("Дерево очищено.")
        
        elif cmd == "dump":
            tree.dump(backup_file)
            print("Резервная копия дерева создана.")
        
        elif cmd == "load":
            tree.load(backup_file)
        
        elif cmd == "exit":
            print("Завершение работы.")
            break
        
        else:
            print("Неизвестная команда.")

if __name__ == "__main__":
    main()
