# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

string = input("введите строку ")
my_string = []
num = 1
for el in range(string.count(' ') + 1):
    my_string = string.split()
    if len(str(my_string)) <= 10:
        print(f" {num} {my_string [el]}")
        num += 1
    else:
        print(f" {num} {my_string [el] [0:10]}")
        num += 1