from figures import Rectangle, Square

print('Изменим ширину и высоту фигур, описанных в коде, нарушающем принцип подстановки Барбары Лисков\n')
# Создаем список фигур
figures = [Rectangle(2, 3), Square(2, 1, 1)]

# Изменяем ширину и высоту каждой фигуры
for figure in figures:
    print("До изменения:", figure)
    figure.set_width(5)
    figure.set_height(10)
    print(f"После изменения:{figure}\n")

print('Для объекта Square это привело к тому, что стороны квадрата перестали оставаться равными.')

from figures import RectangleCorrected, SquareCorrected

print("\nТестируем исправленную реализацию (LSP):")
figures = [RectangleCorrected(2, 3), SquareCorrected(2, 1, 1)]

for figure in figures:
    print("До изменения:", figure)
    figure.width = 5
    figure.height = 10
    print(f"После изменения: {figure}\n")

print('Для объекта SquareCorrected стороны квадрата всегда остаются равными после изменений.\n')