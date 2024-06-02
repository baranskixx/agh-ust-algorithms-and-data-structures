from kol2testy import runtests
from collections import deque

"""
Autor rozwiązania: Adam Barański

Złożoność obliczeniowa: O(V + E) 
Idea:
Rozszerzamy graf -> z kazdego wierzcholka robimy 16 (w zaleznosci od ilosci godzin, ktore mozemy
jeszcze podrozowac bez spania)
Korzystamy z faktu, ze krawedzie sa dlugosci maksymalnie 16, i korzystajac z BFS uruchamiamy 
wyszukiwanie najkrotszej sciezki
"""

INF = 1e9

def build_graph(E):
    n = max(
        max(E, key = lambda x : x[0])[0], 
        max(E, key = lambda x : x[1])[1]
      ) + 1
    G = [[] for _ in range(n)]

    for u, v, c in E:
        G[u].append((v, c))
        G[v].append((u, c))
    
    return G

def warrior(G, s, t):
    G = build_graph(G)
    D = [[INF] * 17 for _ in range(len(G))]
    Q = deque()

    Q.appendleft((s, 0, 16, 0))

    while len(Q) != 0:
        u, d, time_left, travel_left = Q.pop()

        if travel_left != 0:
            Q.appendleft((u, d, time_left, travel_left - 1))
            continue
        
        if d >= D[u][time_left]:
            continue
        
        D[u][time_left] = d

        for v, dist_to_v in G[u]:
            if time_left - dist_to_v >= 0 and D[v][time_left - dist_to_v] > d + dist_to_v:
                Q.appendleft((v, d + dist_to_v, time_left - dist_to_v, dist_to_v))

        if v != s:
            time_left = 16
            d += 8
            for v, dist_to_v in G[u]:
                if time_left - dist_to_v >= 0 and D[v][time_left - dist_to_v] > d + dist_to_v:
                    Q.appendleft((v, d + dist_to_v, time_left - dist_to_v, dist_to_v))

    return min(D[t])
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )

  