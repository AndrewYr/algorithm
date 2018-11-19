# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.

import random

def partition(array, left, right):
    rem = array[(left + right) // 2]
    while left <= right:
        while array[left] < rem:
            left += 1
        while array[right] > rem:
            right -= 1

        if left == right:
            return right
        elif left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return right


def mediana(array):
    center =len(array) // 2
    left = 0
    right = len(array) - 1

    while (True):
        mid = partition(array, left, right)

        if mid == center:
            return array[mid]

        if center < mid:
            right = mid
        else:
            left = mid + 1

array = [random.randint(0, 100) for i in range(9)]
print(array)
print(mediana(array))

# почемуто он работает не постоянно, через раз получается верный вариант

def combsort(array):
    alen = len(array)
    gap = (alen * 10 // 13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:    ## variant "comb-11"
            gap = 11
        swapped = False
        for i in range(alen - gap):
            if array[i + gap] < array[i]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped
    center = len(array) // 2 + 1
    return array[center]

array = [random.randint(0, 100) for i in range(9)]
print(array)
print(combsort(array))