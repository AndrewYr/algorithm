#9 Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))
if (a<b and b<c):
    print(b)
elif (c<b and b<a):
    print(b)
elif (a<c and c<b):
    print(c)
elif (b<c and c<a):
    print(c)
elif (c<a and a<b):
    print(a)
elif (b<a and a<c):
    print(a)
