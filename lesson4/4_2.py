#Представлен список чисел.
#Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.

my_list = [15, 2, 3, 1, 7, 5, 4, 10]
my_new = [el for i, el in enumerate(my_list) if my_list[i] > my_list[i - 1]]
print(f'Первый список {my_list}')
print(f'Полученный список {my_new}')

