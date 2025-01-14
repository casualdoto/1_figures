from Shape import Shape

class RectangleCorrected(Shape):
    """Прямоугольники"""
    name = 'прямоугольник'

    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return (f"{Shape.__repr__(self)}, со сторонами {self.width} и {self.height},"
                f" с площадью {self.area()} и периметром {self.perimeter()}")