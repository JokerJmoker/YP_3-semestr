import math

class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __mul__(self, k):
        return Vec2d(self.x * k, self.y * k)

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def int_pair(self):
        return int(self.x), int(self.y)

    def __repr__(self):
        return f"Vec2d({self.x}, {self.y})"
