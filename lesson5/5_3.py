#Создать текстовый файл (не программно).
#Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
#Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
#Выполнить подсчёт средней величины дохода сотрудников.

my_file = open("5_3.txt", "r")
my_list = my_file.readlines()
s = 0
for i in range(len(my_list)):
    r = my_list[i].split()
    s = s + int(r[1])
    if int(r[1]) < 20000:
        print(r[0])

print(f'Средняя величина дохода {s / len(my_list)}')
