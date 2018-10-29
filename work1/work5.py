# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
import string

#a = str(input('Введите очередность первой буквы: '))
#b = str(input('Введите очередность второй буквы: '))

#list1 = ('abcdefghijklmnopqrstuvwxyz')

#leter1 = list1.rfind(a)+1
#leter2 = list1.rfind(b)+1

#print(f'Первая буква на {leter1} месте')
#print(f'Вторая буква на {leter2} месте')
#print(f'Между мервой и второй буквой {leter2-leter1-1}')

a = input('Введите первый символ буквы: ')
b = input('Введите второй символ буквы: ')

list1 = string.ascii_lowercase

leter1 = list1.rfind(a)+1
leter2 = list1.rfind(b)+1

if leter1 > leter2:
    gap = leter1 - leter2
elif leter1 < leter2:
    gap = leter2 - leter1

print('Буква {} находится на '.format(a) + str(leter1) + ' месте')
print('Буква {} находится на '.format(b) + str(leter2) + ' месте')
print('Между буквами {} и {} {} буквы'.format(a,b,gap))
