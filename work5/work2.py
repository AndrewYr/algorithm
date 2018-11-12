# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque, Counter

letter = Counter({'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})
num = Counter({10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})
first = deque(input('Введите первое число в шестнадцатеричной системе счисления: '))

first.reverse()
second = deque(input('Введите второе число в шестнадцатеричной системе счисления: '))
second.reverse()

_sum = deque()
_pro = deque()

if len(first) > len(second):
    length = len(first)
else:
    length = len(second)

if len(first) < length:
    for _ in range(len(first), length):
        first.append('0')
if len(second) < length:
    for _ in range(len(second), length):
        second.append('0')

reminder = 0
for i in range(length):
    if not first[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        num_first = letter.get(first[i])
    else:
        num_first = first[i]
    if not second[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        num_second = letter.get(second[i])
    else:
        num_second = second[i]
    total = int(num_first) + int(num_second) + reminder
    reminder = 0

    if total >= 10 and total < 16:
        total = num.get(total)
    elif total < 10:
        total = total
    else:
        # reminder = 1
        reminder = total //16
        total = total % 16
        if total < 10:
            total = total
        else:
            total = num.get(total)

    _sum.appendleft(total)

if reminder != 0:
    _sum.appendleft(reminder)

print(_sum)

reminder = 0
for i in second:
    if not i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        num_second_i = letter.get(i)
    else:
        num_second_i = i

    for j in first:
        if j != '0':
            if not j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num_first_j = letter.get(j)
            else:
                num_first_j = j

            total = (int(num_first_j) * int(num_second_i)) + reminder

            reminder = 0
            if total >= 10 and total < 16:
                total = num.get(total)
            elif total < 10:
                total = total
            else:
                reminder = total //16
                total = total % 16
                if total < 10:
                    total = total
                else:
                    total = num.get(total)
        else:
            total = reminder
        _pro.appendleft(total)

print(_pro)
