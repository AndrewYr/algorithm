# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.


import random
a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))

print(f"случайное целое число {random.randrange(a,b)}")
print(f"случайное вещественное число {random.uniform(a,b)}")

a = input('Введите первый символ буквы: ')
b = input('Введите второй символ буквы: ')

list1 = ('abcdefghijklmnopqrstuvwxyz')

leter1 = list1.rfind(a)
leter2 = list1.rfind(b)
print(list1[random.randrange(leter1,leter2)])


