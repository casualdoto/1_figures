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

