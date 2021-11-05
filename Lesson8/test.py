numb_1 = int(input("Введите первое целое число: "))
numb_2 = int(input("Введите второе целое число: "))

if numb_1 != numb_2:
    print("Числа не равны")
    if numb_1 > numb_2:
        print("Первое число больше второго")
    elif numb_2 < numb_1:
        print("Первое число меньше второго")
elif numb_1 == numb_2:
    print("Числа равны")