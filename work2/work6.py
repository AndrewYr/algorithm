# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное пользователем число.
# Если за 10 попыток число не отгадано, то вывести его.
import random

print('Игра угадай число от 1 до 100 (у вас есть 10 попыток)')
random_number = random.randrange(1, 100)
option = int(input('Введите ваш вариант '))

i = 0
while i < 9:
    if option == random_number:
        break
    else:
        if option > random_number:
            print('Вы введи число больше чем нужно')
        else:
            print('Вы введи число меньше чем нужно')
    i += 1
    option = int(input('Введите ваш вариант '))
if i == 9:
    print(f'Увы у вас не получилось угадать число оно на самом деле {random_number}')
else:
    print(f'Поздравляю вы угадали с {i+1} попытки, это число {option}')