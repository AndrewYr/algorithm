# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
even = str()
not_even = str()
i = 0
number = str(input('Введите натуральное число'))
while i < len(number):
    # print('индекс числа:', i, 'число соответствующее индексу', number[i])
    if int(number[i]) % 2:
        not_even = not_even + number[i]
    else:
        even = even + number[i]
    i += 1
print(f'Четные {even} Не четные {not_even}')
