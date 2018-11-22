# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
# beep boop beer!
from collections import Counter,namedtuple
import heapq


class MyNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


text = Counter(input('Введите строку из трех слов'))

t = text.most_common()
t.reverse()
print(t)
