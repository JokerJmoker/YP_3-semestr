import pickle

class Node:
    def __init__(self, key):
        self.left = None # сслыка не левый узел 
        self.right = None # ссылка на правый узел 
        self.val = key # значение узла, которое передается при его созданни

class Tree:
    def __init__(self):
        self.root = None

    # добавление элементов в дерево
    def add(self, key):
        if self.root is None: # если корня нет, то создается узел, который будет корнем
            self.root = Node(key)
        else:
            self._add(self.root, key)

    # рекурсивное добавление узла в ветки дерева (L R в зависимости от значения относительно текущего узла)
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

    # поиск инфы об элементе: True/False, уровень , направление(типо ветка подветки ветки)
    def find(self, key):
        found, level, direction = self._find(self.root, key, 0, None)
        return found, level, direction

    # рекурсивный поиск элемента в дереве
    def _find(self, root, key, level, direction):
        if root is None:
            return False, -1, None  
        if root.val == key:
            return True, level, direction  
        elif key < root.val:
            return self._find(root.left, key, level + 1, 'L')  # ищем в левом поддереве
        else:
            return self._find(root.right, key, level + 1, 'R')  # ищем в правом поддереве

    # по аналогии
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
            # замена узлов (удаленного на минимальный из правой ветки)
            min_larger_node = self._find_min(root.right)
            root.val = min_larger_node.val
            root.right = self._delete(root.right, min_larger_node.val)
        return root

    # движение от правого узла к левому
    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root  # начать с корня, если вызвано без аргументов
        if node is not None:
            print(f"Level {level} - {prefix}{node.val}")  # вывод уровня узла и его значения
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
        with open(filename, 'wb') as f: # write bytes
            pickle.dump(self.root, f)

    def load(self, filename):
        try:
            with open(filename, 'rb') as f: # read bytes 
                self.root = pickle.load(f)
            print("Дерево восстановлено из резервной копии.")
        except FileNotFoundError:
            print("Резервная копия не найдена.")
        except (pickle.UnpicklingError, EOFError, AttributeError) as e:
            print("Ошибка: файл резервной копии поврежден или недоступен.", str(e))

# каждый узел - экземпляр Node 
# val - значение, хранящееся в этом узле 
# left right -  ссылки на узел
# Node(val=5, left=node_3, right=node_7) - под node_3 и node_7 подразумеваются числа 3 и 7
