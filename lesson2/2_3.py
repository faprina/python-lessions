# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

my_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
my_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Введите номер месяца "))
if month ==1 or month == 2 or month == 12:
    print(my_list[month-1])
    print(my_dict.get(1))
elif month == 3 or month == 4 or month ==5:
    print(my_list[month - 1])
    print(my_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(my_list[month - 1])
    print(my_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(my_list[month - 1])
    print(my_dict.get(4))
else:
    print ("Не существует")