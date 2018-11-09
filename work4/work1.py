# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# на примере пятой задачи из прошлого урока
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import cProfile
# import time
# import timeit
import random

def max_num(x):
    array = [random.randint(-100, -1) for _ in range(x)]
    max_num = array[0]
    for i in range(len(array) - 1):
        num = array[i]
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                num = array[i]
                break
        if num > max_num:
            max_num = num

# "work1.max_num(100)"
# 100 loops, best of 5: 186 usec per loop
# "work1.max_num(1000)"
# 100 loops, best of 5: 2.43 msec per loop
# "work1.max_num(10000)"
# 100 loops, best of 5: 59.9 msec per loop

# cProfile.run('max_num(100)')
# 1    0.000    0.000    0.000    0.000 work1.py:13(max_num)
# cProfile.run('max_num(1000)')
# 1    0.001    0.001    0.003    0.003 work1.py:13(max_num)
# cProfile.run('max_num(10000)')
# 1    0.041    0.041    0.062    0.062 work1.py:13(max_num)


def max_num_new(x):
    array = [random.randint(-100, -1) for _ in range(x)]
    max_num = float('-inf')
    for i in array:
        if max_num < i and i < 0:
            max_num = i

# work1.max_num_new(100)
# 100 loops, best of 5: 122 usec per loop
# work1.max_num_new(1000)
# 100 loops, best of 5: 1.2 msec per loop
# work1.max_num_new(10000)
# 100 loops, best of 5: 12.3 msec per loop

# cProfile.run('max_num_new(100)')
# 1    0.000    0.000    0.000    0.000 work1.py:47(max_num_new)
# cProfile.run('max_num_new(1000)')
# 1    0.000    0.000    0.002    0.002 work1.py:47(max_num_new)
# cProfile.run('max_num_new(10000)')
# 1    0.000    0.000    0.020    0.020 work1.py:47(max_num_new)


def max_num_new_f(x):
    array = [random.randint(-100, -1) for _ in range(x)]
    max(array)

# "work1.max_num_new_f(100)"
# 100 loops, best of 5: 119 usec per loop
# "work1.max_num_new_f(1000)"
# 100 loops, best of 5: 1.2 msec per loop
# "work1.max_num_new_f(10000)"
# 100 loops, best of 5: 12.4 msec per loop


# cProfile.run('max_num_new_f(100)')
# 1    0.000    0.000    0.000    0.000 work1.py:60(max_num_new_f)
# cProfile.run('max_num_new_f(1000)')
# 1    0.000    0.000    0.002    0.002 work1.py:60(max_num_new_f)
# cProfile.run('max_num_new_f(10000)')
# 1    0.000    0.000    0.019    0.019 work1.py:60(max_num_new_f)


# Впринциве второй и третий вариант решения по скорости одинаковые, но скорее всего третий вариант кушает больше ресурсов чем второй.
