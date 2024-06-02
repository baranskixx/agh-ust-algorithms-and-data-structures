
"""
Autor rozwiazania: Adam Barański
Złozonosc czasowa: O(E * logV)
Złozonosc pamieciowa: O(E * logV)

Idea:
Tworzymy graf o rozmiarze 2*V, 
Pierwsze V wierzcholkow odpowiada wierzcholkom w sytuacji, kiedy mozliwe jest uzycie dwumilowych butow
Kolejne V - kiedy uzycie nie jest mozliwe

Sprawdzamy minimalny koszt dotarcia z wierzcholka s do t lub V + t
"""

from zad3testy import runtests
from queue import PriorityQueue

INF = 1e9

def build_modified_graph(old_graph):
    n = len(old_graph)
    G = [[INF] * (2 * n) for _ in range(2 * n)]

    for u in range(n):
        for v in range(n):
            c1 = old_graph[u][v]
            if c1 != 0:
                G[u][v] = c1
                G[n + u][v] = c1
                for x in range(n):
                    c2 = old_graph[v][x]
                    if c1 != 0 and c2 != 0:
                        G[u][n+x] = min(G[u][n+x], max(c1, c2))

    return G

def jumper(G, s, t):
    n = len(G)
    G = build_modified_graph(G)

    D = [INF] * (2 * n)
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        c, v = Q.get()

        if c >= D[v]:
            continue

        D[v] = c
        for u in range(2 * n):
            if G[v][u] == INF:
                continue
            if D[u] > G[v][u] + c:
                Q.put((G[v][u] + c, u))
    
    return min(D[t], D[n+t])


runtests(jumper)
