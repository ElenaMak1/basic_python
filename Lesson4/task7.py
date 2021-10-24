from math import factorial

def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)

print("<<Программа вычисления факториала числа>>")
for el in factorial_gen(15):
    print(el)