from abc import *
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.14159 * self.radius ** 2


class Tringula(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def checkExist(self):
        a, b, c = self.a, self.b, self.c
        if a + b <= c or a + c <= b or b + c <= a:
            return False
        return True

    def area(self):
        if not self.checkExist():
            return -1
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def isRight(self):
        if not self.checkExist():
            return -1
        a, b, c = self.a, self.b, self.c
        sides = sorted([a, b, c])
        a, b, c = sides
        return abs(a ** 2 + b ** 2 - c ** 2) < 1e-10


