from Rectangle import Rectangle
from Square import Square
from RectangleCorrected import RectangleCorrected
from SquareCorrected import SquareCorrected

# Изменим ширину и высоту фигур, описанных в коде, нарушающем принцип подстановки Барбары Лисков
figures = [Rectangle(2, 3), Square(2, 1, 1)] # Создаем список фигур

# Изменяем ширину и высоту каждой фигуры
for figure in figures:
    print("До изменения:", figure)
    figure.set_width(5)
    figure.set_height(10)
    print(f"После изменения:{figure}\n")

# Для объекта Square это привело к тому, что стороны квадрата перестали оставаться равными


# Тестируем исправленную реализацию (LSP):
figures = [RectangleCorrected(2, 3), SquareCorrected(2, 1, 1)] # Создаем список фигур

# Изменяем ширину и высоту каждой фигуры
for figure in figures:
    print("До изменения:", figure)
    figure.width = 5
    figure.height = 10
    print(f"После изменения: {figure}\n")

# Для объекта SquareCorrected стороны квадрата всегда остаются равными после изменений