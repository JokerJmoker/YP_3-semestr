import pickle

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add(self.root, key)

    def _add(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._add(root.left, key)
        elif key > root.val:
            if root.right is None:
                root.right = Node(key)
            else:
                self._add(root.right, key)

    def find(self, key):
        found, level, direction = self._find(self.root, key, 0, None)
        return found, level, direction

    def _find(self, root, key, level, direction):
        if root is None:
            return False, -1, None  # Не найдено
        if root.val == key:
            return True, level, direction  # Найдено, возвращаем уровень и направление
        elif key < root.val:
            return self._find(root.left, key, level + 1, 'L')  # Ищем в левом поддереве
        else:
            return self._find(root.right, key, level + 1, 'R')  # Ищем в правом поддереве

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_larger_node = self._find_min(root.right)
            root.val = min_larger_node.val
            root.right = self._delete(root.right, min_larger_node.val)
        return root

    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root  # Начать с корня, если вызвано без аргументов
        if node is not None:
            print(f"Level {level} - {prefix}{node.val}")  # Вывод уровня узла и его значения
            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")

    def show_commands(self):
        commands = """
        Доступные команды:
        1. add X - добавить элемент в дерево (только целые числа)
        2. find X - найти элемент в дереве
        3. delete X - удалить элемент из дерева
        4. print - распечатать все элементы дерева в отсортированном порядке
        5. clear - очистить дерево
        6. dump - создать резервную копию дерева
        7. load - загрузить дерево из резервной копии
        8. exit - завершить работу
        """
        print(commands)
        
    def clear(self):
        self.root = None

    def dump(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.root, f)

    def load(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.root = pickle.load(f)
            print("Дерево восстановлено из резервной копии.")
        except FileNotFoundError:
            print("Резервная копия не найдена.")
        except (pickle.UnpicklingError, EOFError, AttributeError) as e:
            print("Ошибка: файл резервной копии поврежден или недоступен.", str(e))
