import math


class Complex():
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part
        pass


    def __add__(self, other):
        # +
        return Complex(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)


    def __sub__(self, other):
        # -
        return Complex(self.real_part - other.real_part, self.imaginary_part - other.imaginary_part)


    def __mul__(self, other):
        # *
        real_part = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        imaginary_part = self.real_part * other.imaginary_part + self.imaginary_part * other.real_part
        return Complex(real_part, imaginary_part)


    def __truediv__(self, other):
        # /
        denominator = other.real_part**2 + other.imaginary_part**2
        real_part = (self.real_part * other.real_part + self.imaginary_part * other.imaginary_part) / denominator
        imaginary_part = (self.imaginary_part * other.real_part - self.real_part * other.imaginary_part) / denominator
        return Complex(real_part, imaginary_part)

   
    def __abs__(self):
        # || 
        return math.sqrt(self.real_part**2 + self.imaginary_part**2)
    
    
    def __str__(self):
        # print 
        if self.imaginary_part >= 0:
            return f"{self.real_part} + {self.imaginary_part}i"
        else:
            return f"{self.real_part} - {abs(self.imaginary_part)}i"
        

a = Complex (5, -6)
b = Complex (7, 8)

print (f'a = {a}')
print (f'b = {b}')
print(f'|{a}| = {abs(a):.2f}')
print (f'a + b = {(a+b)}\n a - b ={(a-b)}\n a * b = {(a*b)}\n a / b = {(a/b)}')
