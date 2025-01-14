from Shape import Shape
from Rectangle import Rectangle

class Square(Rectangle):
    """Квадраты"""
    name = 'квадрат'

    def __init__(self, side, x=0, y=0):
        super().__init__(side, side, x, y)

    def __repr__(self):
        return (f"{Shape.__repr__(self)}, со стороной {self.width},"
                f" с площадью {self.area()} и периметром {self.perimeter()}")
