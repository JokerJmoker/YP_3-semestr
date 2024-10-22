from classes import BST  # Импортируем BST из bst.py

def main():
    bst = BST()
    backup_file = 'tree_backup.pkl'
    
    # Вывод доступных команд при старте программы
    bst.show_commands()
    
    while True:
        command = input("Введите команду: ").strip().split()
        
        if len(command) == 0:
            continue
        
        cmd = command[0]
        
        if cmd == "add":
            if len(command) > 1:
                try:
                    bst.add(int(command[1]))
                except ValueError:
                    print("Ошибка: Необходимо ввести целое число.")
            else:
                print("Ошибка: Необходимо указать число.")
        
        elif cmd == "find":
            if len(command) > 1:
                try:
                    found, level, direction = bst.find(int(command[1]))
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
                    bst.delete(int(command[1]))
                except ValueError:
                    print("Ошибка: Необходимо ввести целое число.")
            else:
                print("Ошибка: Необходимо указать число.")
        
        elif cmd == "print":
            bst.print_tree()
        
        elif cmd == "clear":
            bst.clear()
            print("Дерево очищено.")
        
        elif cmd == "dump":
            bst.dump(backup_file)
            print("Резервная копия дерева создана.")
        
        elif cmd == "load":
            bst.load(backup_file)
        
        elif cmd == "exit":
            print("Завершение работы.")
            break
        
        else:
            print("Неизвестная команда.")

if __name__ == "__main__":
    main()
