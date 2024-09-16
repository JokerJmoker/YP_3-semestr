import math

class Vector:
    def __init__(self, x, y=None, z=None):
        if isinstance(x, str):
            x = x.strip().replace('(', '').replace(')', '')
            coords = x.split(',')
            if len(coords) == 1:
                self.x = float(coords[0])
                self.y = 0.0
                self.z = 0.0
            elif len(coords) == 2:
                self.x = float(coords[0])
                self.y = float(coords[1])
                self.z = 0.0
            elif len(coords) == 3:
                self.x = float(coords[0])
                self.y = float(coords[1])
                self.z = float(coords[2])
            else:
                raise ValueError("Координаты должны быть заданы в формате (x,y,z)")
        else:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
 
    # print
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    # + 
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # -
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # *
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    # /
    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot divide by zero.")
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    # ==
    def __eq__(self, other):

        return self.x == other.x and self.y == other.y and self.z == other.z
    

    # Метод для второго задания
    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)