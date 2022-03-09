#1Поработайте с переменными, создайте несколько,выведите на экран
#запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 10
b = 15
print("Переменные a и b - ", a, b)
string1 = input("Введите 1 строку ")
string2 = input("Введите 2 строку ")
number1 = int(input("Введите 1 число "))
number2 = int(input("Введите 2 число "))
print("Введеные значения - %10s %10s %5d %5d" % (string1, string2, number1, number2))

#2Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

#3Узнайте у пользователя число n.
#Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369


n = int(input("Введите число "))
a = int(str(n) + str(n))
b = int(str(n) + str(n) + str(n))
sum = (n + a + b)
print("Сумма чисел n + nn + nnn %d" % sum)


#4Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break

#5 Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма
#(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение.

profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print("Фирма работает с прибылью")
else:
    print("Фирма работает в убыток")

#6 Если фирма отработала с прибылью,
#вычислите рентабельность выручки (соотношение прибыли к выручке).
#Далее запросите численность сотрудников фирмы
#и определите прибыль фирмы в расчете на одного сотрудника.

profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль в расчете на одного сторудника {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")


#7 Спортсмен занимается ежедневными пробежками.
#В первый день его результат составил a километров.
#Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
#Требуется определить номер дня, на который общий результат спортсмена составит не менее b километров.
#Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input("Введите результаты пробежки 1 дня (км) "))
b = int(input("Введите общий желаемый результат (км) "))
result_d = 1
result_km = a
while result_km < b:
        a = a + a * 0.1
        result_d += 1
        result_km = result_km + a
print("Вы достигнете требуемых показателей на %.d день" % (result_d))

