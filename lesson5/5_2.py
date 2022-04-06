#Создать текстовый файл (не программно), сохранить в нём несколько строк,
#выполнить подсчёт строк и слов в каждой строке.

my_file = open('5_2.txt', "r")
content = my_file.read()
print(f'содержимое \n {content}')
my_file = open('5_2.txt', "r")
content = my_file.readlines()
print(f'количество строк - {len(content)}')
for i in range(len(content)):
    print(f'количество слов в строке {i + 1}: {len(content[i].split())}')
my_file.close()
