# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.
import random


def bubble(array):
    n = 1
    cont = False
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            cont = True
            break
    if cont:
        n = 1
        while n < len(array):
            for i in range(len(array) - 1):
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    # print('\t' + str(array))
            # print(array)
            n += 1


array = [random.randint(-100, 100) for i in range(10)]
# array = [1, 2, 3, 4, 5]
print(array)
bubble(array)
print(array)
