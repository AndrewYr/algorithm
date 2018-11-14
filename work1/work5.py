# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
import string

a = input('Введите первый символ буквы: ')
b = input('Введите второй символ буквы: ')

list1 = string.ascii_lowercase

leter1 = list1.rfind(a) + 1
leter2 = list1.rfind(b) + 1

if leter1 > leter2:
    gap = leter1 - leter2
elif leter1 < leter2:
    gap = leter2 - leter1

print('Буква {} находится на '.format(a) + str(leter1) + ' месте')
print('Буква {} находится на '.format(b) + str(leter2) + ' месте')
print('Между буквами {} и {} {} буквы'.format(a, b, gap))

# Разбор на уроке
first = ord(input('1-я буква: '))
second = ord(input('2-я буква: '))

first = first - ord('a') + 1
second = second - ord('a') + 1

print(f'Порядковый номер 1-ой буквы {first} 2-ой буквы {second}')
print(f'Число букв между введеными: {abs(first - second) - 1}')

a = string.ascii_letters
print(a)