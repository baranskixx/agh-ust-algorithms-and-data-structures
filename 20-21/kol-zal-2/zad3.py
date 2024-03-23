from zad3testy import runtests
from queue import PriorityQueue

"""
Autor rozwiazania: Adam Baranski

Złożoność obliczeniowa: O(|E| * log|V|})
Idea:
Dijkstra z dwoch punktow (s i t), sprawdzamy wszystkie krawedzie czy naleza do minimalnej sciezki
Po zliczeniu zwracamy wynik
"""

INF = 1e10

def paths(G,s,t):
    n = len(G)
    
    D = [[INF]*n for _ in range(2)]

    Q = PriorityQueue()
    START_V = [s, t]
    for i in range(2):
        Q.put((0,START_V[i]))

        while not Q.empty():
            d, u = Q.get()
            if d >= D[i][u]:
                continue

            D[i][u] = d
            for v, c in G[u]:
                if D[i][u] + c < D[i][v]:
                    Q.put((D[i][u] + c, v))
    result = 0
    for u in range(n):
        for v, d in G[u]:
            if v > u and (D[0][u] + D[1][v] + d == D[0][t] or D[1][u] + D[0][v] + d == D[0][t]):
                result += 1
    
    return result

    
runtests( paths )


