# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

text = input('Введите строку: ')
first = 0
second = 1
st = set()
def h_text(text,first,second):
    long = len(text)+1
    second_s = second

    while True:
        for first in range(second):
            sss = text[first:second]
            if sss != text:
                print(sss)
                st.add(hash(sss))
        second += 1
        if second == long:
            return len(st)

print(h_text(text,first,second))
