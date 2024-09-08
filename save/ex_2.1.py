"""
Напишите программу, которая объявляет класс Shape, конструктор которого принимает ширину и высоту.
После этого унаследуйте от него класс Triangle и Rectangle. Реализуйте метод area(), который возвращает площадь этих фигур.
Продемонстрируйте работоспособность программы.
"""

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def area(self):
        return 1/2 * self.width * self.height

class Rectangle(Shape):
    def area(self):
        return self.width * self.height

triangle = Triangle(4.33, 2.12)
rectangle = Rectangle(4.11, 2.33)

print(f"Площадь треугольника:  {triangle.area():.2f} ")
print(f"Площадь прямоугольника: {rectangle.area():.2f}")
