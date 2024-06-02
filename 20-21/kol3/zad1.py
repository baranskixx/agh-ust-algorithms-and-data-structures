"""
Autor rozwiązania: Adam Barański

Złożoność obliczeniowa: O(n ^ 4) 
Idea:
Budujemy graf, ktorego pojedynczy wierzcholek okreslaja pozycje Karola i Maxa
Krawedz pomiedzy dwoma wierzcholkami w takim grafie istnieje, jesli 
mozemy w jednym ruchu przejsc z jednej pozycji obu panow do innej

W takim grafie szukamy dowolnej sciezki z (s, t) do (t, s)
"""

from zad1testy import runtests
from math import inf
from copy import deepcopy

def floyd_warshall(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            if i != j and T[i][j] == 0:
                T[i][j] = 1e10

    for i in range(n):
        for j in range(n):
            if j != i:
                for k in range(n):
                    if k != j and k != i:
                        T[i][j] = min(T[i][j], T[i][k] + T[k][j])

def keep_distance(M, x, y, d):
    n = len(M)
    _start = x * n + y
    _end   = y * n + x
    n = len(M)
    T = deepcopy(M)
    floyd_warshall(T)
    print(T)
    G = [[] for _ in range(n ** 2)]

    for x in range(n):
        for y in range(n):
            if T[x][y] >= d:
                print(x, y)
                index = x + n * y
                for chgx in range(n):
                    for chgy in range(n):
                        if M[y][chgy] != 0 and M[x][chgx] and T[x][chg] >= d:
                            neigh_index = x + n * chg
                            G[index].append(neigh_index)
                        if M[x][chg] != 0 and T[chg][y] >= d:
                            neigh_index = chg + n * y
                            G[index].append(neigh_index)
                        
    V = [False] * (n**2)
    res = []
    print(G)
    
    def dfs(u):
        if u == _end:
            res.append(u)
        V[u] = True

        for v in G[u]:
            if not V[v]:
                if dfs(v):
                    res.append(u)
                    return True
        return False
    
    dfs(_start)

    return [(x%n, x//n) for x in res][::-1]



runtests(keep_distance)