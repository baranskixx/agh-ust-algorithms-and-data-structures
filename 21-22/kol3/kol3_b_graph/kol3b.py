from kol3btesty import runtests
from queue import PriorityQueue

"""
Autor rozwiazania: Adam Baranski

Złozonosc obliczeniowa: O (E * log V)
Zlozonosc pamieciowa: O (E * log V)

Algorytm Dijkstry po grafie G z dodatkowym uwzględnieniem przelotów z tabeli A
"""
def airports( G, A, s, t ):
    n = len(G)
    INF = 1e12
    D = [INF] * n
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty() and D[t] == INF:
        c, u = Q.get()

        if D[u] <= c:
            continue
        D[u] = c

        for v, d in G[u]:
            if D[v] > D[u] + d:
                Q.put((D[u] + d, v))
        for v, d in enumerate(A):
            if v != u and D[v] > d + A[u] + c:
                Q.put(( d + A[u] + c, v))

    return D[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )