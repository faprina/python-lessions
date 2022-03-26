#Реализовать функцию my_func(), которая принимает три позиционных аргумента
#и возвращает сумму наибольших двух аргументов

def my_f(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a > b and c > a:
        return a + c
    else:
        return b + c

arg1 = int(input("введите 1 аргумент "))
arg2 = int(input("введите 2 аргумент "))
arg3 = int(input("введите 3 аргумент "))
print(my_f(arg1, arg2, arg3))