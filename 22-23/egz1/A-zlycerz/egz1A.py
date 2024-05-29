from egz1Atesty import runtests
from queue import PriorityQueue
"""
Autor rozwiazania: Adam Barański
Złozonosc czasowa: O(n * E)
Złozonosc pamieciowa: O(n * E)

Idea:
Tworzymy graf o rozmiarze 2*V, 
Pierwsze V wierzcholkow odpowiada zamkom przed obrabowaniem
Kolejne V - zamki po obrabowaniu

Sprawdzamy minimalny koszt dotarcia z wierzcholka s do V+t
"""

INF = 1e10

class Node:
    def __init__(self):
        self.neigh = []
    
    def add_egde(self, dir, cost):
        self.neigh.append((dir, cost))


def gold(G,V,s,t,r):
    n = len(G)
    # Przygotowanie grafu
    GRAPH = [Node() for _ in range(2 * n)]
    for u in range(n):
        GRAPH[u].add_egde(n + u, -V[u])
        for v, c in G[u]:
            GRAPH[u].add_egde(v, c)
            GRAPH[n + u].add_egde(n + v, c * 2 + r)
    
    Q = PriorityQueue()
    D = [INF] * (2 * n)
    Q.put((0, s))

    while not Q.empty():
        d, u = Q.get()

        if D[u] < d:
            continue
        D[u] = d

        for v, c in GRAPH[u].neigh:
            if D[v] > d + c:
                Q.put((d+c, v))
    
    return min(D[t], D[t+n])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
