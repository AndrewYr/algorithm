# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

a = str(input('Введите очередность первой буквы: '))
b = str(input('Введите очередность второй буквы: '))

list1 = ('abcdefghijklmnopqrstuvwxyz')

leter1 = list1.rfind(a)+1
leter2 = list1.rfind(b)+1

print(f'Первая буква на {leter1} месте')
print(f'Вторая буква на {leter2} месте')
print(f'Между мервой и второй буквой {leter2-leter1-1}')
