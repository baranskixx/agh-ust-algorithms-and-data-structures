from zad1testy import runtests
from collections import deque

"""
Autor rozwiazania: Adam Barański
Złozonosc czasowa: O(n)
Złozonosc pamieciowa: O(E * logV)

Idea:
Tworzymy kolejke dla kazdej litery, w kolejkach zapisujemy indeksy, 
pod ktorymi literka wystepuje dla pierwszego slowa
Przechodzimy przez y
"""

def tanagram(x, y, t):
    if len(x) != len(y):
        return False
    
    n = len(x)
    letters = [deque() for _ in range(26)]
    
    for i, ch in enumerate(x):
        queue_index = ord(ch) - ord('a')
        letters[queue_index].append(i)
    
    for i, ch in enumerate(y):
        queue_index = ord(ch) - ord('a') 
        if len(letters[queue_index]) == 0:
            return False
        diff = abs(i - letters[queue_index].popleft())
        if diff > t:
            return False
    
    return True
    
runtests(tanagram)
