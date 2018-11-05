# 4. Определить, какое число в массиве встречается чаще всего.

import random

array = [random.randint(0, 10) for _ in range(100)]
print(array)
len(array)
num = array[0]
max_repeat = 1
for i in range(len(array) - 1):
    repeat = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            repeat += 1
    if repeat > max_repeat:
        max_repeat = repeat
        num = array[i]

if max_repeat > 1:
    print(f'{max_repeat} раз встречается число {num}')
else:
    print('Все элементы уникальны')
