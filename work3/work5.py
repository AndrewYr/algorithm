# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

array = [random.randint(-100, -1) for _ in range(30)]
print(array)

max_num = array[0]
position = 0
for i in range(len(array) - 1):
    num = array[i]
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            num = array[i]
            break
    if num > max_num:
        max_num = num
        position = i
print(f'максимальное из отрицательных число{max_num} находится на позиции {position}')
