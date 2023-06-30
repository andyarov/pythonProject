'''class Rectangle():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        sq = self.a * self.b
        return sq


rect = Rectangle(4, 5)
print(rect.square())'''
from math import pi


class Circle():
    def __init__(self, r):
        self.r = r

    def square(self):
        sq = pi * (self.r ** 2)
        return sq

    def perimetr(self):
        c = pi * self.r * 2
        return c


circle = Circle(6)
print('sq=', circle.square(), 'c=', circle.perimetr())
