import math 

class Vec2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError(":0 !")
        return Vec2D(self.x / scalar, self.y / scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self): # возвращает длину вектора через встроенную функцию len().
        return int(self.length())

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def int_pair(self):  # возвращает кортеж из двух целых чисел, представляющих координаты вектора.
        return int(self.x), int(self.y)
