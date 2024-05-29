from zad3testy import runtests
from queue import PriorityQueue

"""
Autor rozwiazania: Adam Baranski

Złozonosc obliczeniowa: O(H * W) 

1. Przy pomocy przeszukiwania w glab badamy laczna ilosc ropy w kazdej plamie,
która ma jakiś swój fragment w pierwszym wierszu, oraz dla kazdej plamy kumulujemy 
cala objetosc plamy w pierwszym (od lewej) punkcie tej plamy w najwyzszym rzedzie
2. Z pomoca kolejki priorytetowej wyznaczamy kolejne wartosci
"""

def modify_board(T):
    h = len(T)
    w = len(T[0])
    V = [[False]*w for _ in range(h)]

    def dfs(y, x):
        if y < 0 or x < 0 or y >= h or x >= w or V[y][x] or T[y][x] == 0:
            return 0
        V[y][x] = True
        tmp = T[y][x]
        T[y][x] = 0

        return tmp + dfs(y-1, x) + dfs(y+1, x) + dfs(y, x-1) + dfs(y, x+1)
    
    for x in range(w):
        if T[0][x] != 0:
            T[0][x] = dfs(0, x)
    
    return T

def plan(T):
    T = modify_board(T)[0]
    Q = PriorityQueue()
    Q.put((-T[0], 0))
    max_travel = 0
    result = []
    while max_travel < len(T)-1:
        fuel, x = Q.get()
        fuel = abs(fuel)

        for i in range(max_travel + 1, min(max_travel + 1 + fuel, len(T))):
            if T[i] != 0:
                Q.put((-T[i], i))
        
        max_travel = max_travel + fuel
        result.append(x)

    return sorted(result)

runtests(plan)
