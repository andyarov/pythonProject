class Rectangle():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self, ):
        sq = self.a * self.b
        return sq


rect = Rectangle(4, 5)
print(rect.square())
