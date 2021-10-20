def calculator(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Ошибка! Делить на ноль нельзя')
print(calculator(int(input('Первое число: ')), int(input('Второе число: '))))