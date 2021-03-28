class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def __str__(self):
        return "Rectangle: width {}, height {} ".format(self.width, self.height)

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


x = Rectangle(10, 14)

print(x)

