from zad1testy import runtests
from queue import PriorityQueue

"""
Autor rozwiązania: Adam Barański
Zlozonosc: O(E * logV)
Dijkstra na rozmnozonym grafie, z zapisywaniem prev wierzcholka
"""

INF = 1e9

def jak_dojade(G, P, d, a, b):
    n = len(G)

    D = [[INF] * (d + 1) for _ in range(n)]
    PREV = [[None] * (d + 1) for _ in range(n)]
    
    FUEL = [False] * n
    for u in P:
        FUEL[u] = True
    
    Q = PriorityQueue()
    Q.put((0, d, a, None))

    while not Q.empty():
        dist, fuel, u, prev = Q.get()
        print(u)

        if D[u][fuel] <= dist:
            continue
        
        D[u][fuel] = dist
        PREV[u][fuel] = prev

        if FUEL[u] and D[u][d] > dist:
            Q.put((dist, d, u, prev))
        
        for v, dist_to_v in enumerate(G[u]):
            if dist_to_v != -1 and fuel >= dist_to_v and D[v][fuel - dist_to_v] > dist + dist_to_v:
                Q.put((dist + dist_to_v, fuel - dist_to_v, v, (u, fuel)))
    
    min_dist = min(D[b])
    if min_dist == INF:
        return None
    
    u = b
    fuel = D[b].index(min_dist)
    path = [b]

    while PREV[u][fuel] is not None:
        u, fuel = PREV[u][fuel]
        path.append(u)
    
    return path[::-1]

runtests( jak_dojade ) 
