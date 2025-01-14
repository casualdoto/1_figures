class Shape:
    """Геометрические фигуры"""
    name = 'геометрическая фигура'

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"{self.name} по координатам ({self.__x}, {self.__y})"

