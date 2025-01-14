from Shape import Shape

class Rectangle(Shape):
    """Прямоугольники"""
    name = 'прямоугольник'

    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def __repr__(self):
        return (f"{Shape.__repr__(self)}, со сторонами {self.width} и {self.height},"
                f" с площадью {self.area()} и периметром {self.perimeter()}")
