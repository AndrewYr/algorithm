# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

array = [random.randint(0, 10) for _ in range(10)]
print(array)

if array[0] > array[1]:
    max_num = array[0]
    min_num = array[1]
    min1 = 1
    max1 = 0
else:
    min_num = array[0]
    max_num = array[1]
    min1 = 0
    max1 = 1

for i in range(2, len(array)):
    if array[i] < array[min1]:
        min1 = i
        min_num = array[i]
    if array[i] > array[max1]:
        max1 = i
        max_num = array[i]
print(f'Минимальное число {min_num} под индексом {min1}')
print(f'Максимальное число {max_num} под индексом {max1}')

sum_num = 0
for i in range(min1+1,max1-1):
    sum_num += array[i]
print(f'Сумма элементов, находящихся между минимальным и максимальным элементами равна {sum_num}')

# Как можно было оптимизировать решение данной задачи?