# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


a = int(input('Введите номер буквы: '))
list1 = ('abcdefghijklmnopqrstuvwxyz')
if a > 26 or a < 1:
    print("Буквы с таким номером нет")
else:
    print(list1[a-1])

