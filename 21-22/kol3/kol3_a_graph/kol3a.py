from kol3atesty import runtests
from queue import PriorityQueue

"""
Autor rozwiazania: Adam Baranski

Złozonosc obliczeniowa: O (E * log V)
Zlozonosc pamieciowa: O (E * log V)

Algorytm Dijkstry po grafie G z dodatkowym uwzględnieniem osobliwości
"""

def spacetravel( n, E, S, a, b ):
    G = [[] for _ in range(n)]
    C = [False] * n

    for s in S:
        C[s] = True
    
    for u, v, c in E:
        G[u].append((v, c))
        G[v].append((u, c))
    
    INF = 1e9
    D = [INF] * n
    Q = PriorityQueue()
    Q.put((0, a))


    while not Q.empty() and D[b] == INF:
        c, u = Q.get()

        if D[u] <= c:
            continue

        D[u] = c

        if C[u]:
            for v in S:
                if v != u and D[v] > D[u]:
                    Q.put((D[u], v))
        for v, c in G[u]:
            if D[v] > D[u] + c:
                Q.put((D[u] + c, v))
        
    return D[b] if D[b] != INF else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )