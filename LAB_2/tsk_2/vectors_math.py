import math

class Vector:
    def __init__(self, x, y=None, z=None):
        if isinstance(x, str):
            x = x.strip("()")
            coords = x.split(",")
            self.x = float(coords[0])
            self.y = float(coords[1]) if len(coords) > 1 else 0.0
            self.z = float(coords[2]) if len(coords) > 2 else 0.0
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
    
    # [a,b]
    @classmethod
    def cross_product(cls, vec1, vec2):
        """Вычисляет векторное произведение двух векторов"""
        x = vec1.y * vec2.z - vec1.z * vec2.y
        y = vec1.z * vec2.x - vec1.x * vec2.z
        z = vec1.x * vec2.y - vec1.y * vec2.x
        return cls(x, y, z)

    # (a,b)
    @staticmethod
    def dot_product(vec1, vec2):
        """Вычисляет скалярное произведение двух векторов"""
        return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z

    @staticmethod
    def get_result_for_several_points(number_of_points,function_for_points,text):
        points = []
    
        for point in range(number_of_points):
            coords = input("Введите координаты точки (x,y,z): ")
            points.append(Vector(coords))

        answer = function_for_points(points)
        return f'{text} , {answer}'
    
    
    @staticmethod
    def input_vector(text):
        coords = input(text).strip() 
        return Vector(coords)  # передача строки в конструктор