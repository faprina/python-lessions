#Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных будет свидетельствовать пустая строка.

my_file = open('5_1.txt', 'w')
line = input('Введите текст \n')
while line:
    my_file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_file.close()
my_file = open('5_1.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()
