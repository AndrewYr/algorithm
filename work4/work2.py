# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile

def easy(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    # print(sieve)
    # res = [i for i in sieve if i != 0]
    # print(res)

# cProfile.run('easy(1000)')
# 1    0.000    0.000    0.000    0.000 work2.py:8(easy)
# cProfile.run('easy(10000)')
# 1    0.003    0.003    0.004    0.004 work2.py:8(easy)
# cProfile.run('easy(100000)')
# 1    0.039    0.039    0.044    0.044 work2.py:8(easy)

# "work2.easy(1000)"
# 100 loops, best of 5: 287 usec per loop
# "work2.easy(10000)"
# 100 loops, best of 5: 3.59 msec per loop
# "work2.easy(100000)"
# 100 loops, best of 5: 45.1 msec per loop



def easy_1(n):
    lst = []
    k = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    # print(lst)

# cProfile.run('easy_1(1000)')
# 1    0.032    0.032    0.032    0.032 work2.py:37(easy_1)
# cProfile.run('easy_1(10000)')
# 1    4.262    4.262    4.262    4.262 work2.py:37(easy_1)
# cProfile.run('easy_1(100000)')
# 1  354.562  354.562  354.566  354.566 work2.py:37(easy_1)

# "work2.easy_1(1000)"
# 100 loops, best of 5: 28.7 msec per loop


# "work2.easy_1(100000)"
# Этого я дожидаться не стал :)




#Нахождение простых чисел с помощью решета Эратосфена калосально быстрее
# Конечно может это связано с тем что во втором вариантемы добавляем в список значения