class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Sqaure(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Sqaure(4, 4)
cube = Cube(4, 4, 4)

print(square.area())
print(cube.volume())
