from zad2testy import runtests
from queue import PriorityQueue

"""
Autor rozwiązania: Adam Barański
Zlozonosc: O(V * log(E))

Djikstra z taka modyfikacja, ze zaczynamy od wszystkich wierzcholkow z pierwsza litera wyrazu a 
na koncu sprawdzamy wszystkie wierzcholki z ostatnia litera
Dodatkowo zapisujemy min koszt dotarcia do wierzcholka w zaleznosci od tego, ktoremu 
"""

INF = 1e9

def let( ch ): return ord(ch) - ord("a")

def letters( G, W ):
    V, E = G

    n = len(V)
    G = [[] for _ in range(n)]
    for u, v, c in E:
        G[u].append((v, c))
        G[v].append((u, c))
    
    Q = PriorityQueue()
    for u in range(n):
        if V[u] == W[0]:
            Q.put((0, u, 0))
    
    D = [[INF] * len(W) for _ in range(n)]

    while not Q.empty():
        d, u, i = Q.get()

        if D[u][i] <= d:
            continue

        D[u][i] = d
        if i != len(W) - 1:
            for v, c in G[u]:
                if V[v] == W[i+1]:
                    Q.put((d + c, v, i+1))
    
    result = INF
    for u in range(n):
        if V[u] == W[-1]:
            result = min(result, D[u][-1])
    
    return result

    

runtests( letters )
    
    
