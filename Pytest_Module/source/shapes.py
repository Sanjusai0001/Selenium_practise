import math

class Shapes:

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shapes):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius



class Rectangle(Shapes):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __int__(self, other):
        if not isinstance(other, Rectangle):
            return False

        return self.breadth == other.breadth and self.length == other.length


    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return (self.length * 2) + ( 2 * self.breadth)


class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(side_length, side_length)