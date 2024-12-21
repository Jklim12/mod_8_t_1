def add_everything_up(a, b):
    try:
        # Пытаемся сложить значения a и b
        return a + b
    except TypeError:
        # Если типы разные, возвращаем строковое представление a и b
        return str(a) + str(b)
print(add_everything_up(123.456, 'строка'))

print(add_everything_up('яблоко', 4215))

print(add_everything_up(123.456, 7))




