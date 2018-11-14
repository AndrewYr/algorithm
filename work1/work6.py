# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string
a = int(input('Введите номер буквы: '))
list1 = string.ascii_lowercase
if a > 26 or a < 1:
    print("Буквы с таким номером нет")
else:
    print(list1[a-1])


num = int(input('Введите номер буквы от 1 до 26: '))
num = ord('a') + num - 1
print(f'Эта буква {chr(num)}')


FIRST_LETTER = 96
num = int(input('Введите номер буквы от 1 до 26: '))
num = FIRST_LETTER + num
print(f'Эта буква {chr(num)}')