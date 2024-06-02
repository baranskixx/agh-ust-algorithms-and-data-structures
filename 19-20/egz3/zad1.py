from zad1testy import runtests
from collections import deque

"""
Autor rozwiązania: Adam Barański

Złożoność obliczeniowa: O(V + E) 
Idea:
2 x BFS
Raz z dowolnego wierzcholka
Drugi raz z najdalszego wierzcholka od pierwszego
"""

def best_root(L):
    n = len(L)
    D = [1e9] * n

    def bfs(start):
        Q = deque()
        Q.append((start, 0))

        while len(Q) != 0:
            u, d = Q.popleft()
            if D[u] <= d:
                continue
            D[u] = d

            for v in L[u]:
                Q.append((v, d+1))
    
    bfs(0)
    furthest = max(range(n), key=lambda x : D[x])
    D = [1e9] * n
    print(furthest)
    bfs(furthest)
    print(D)
    return D.index(max(D) // 2)



runtests( best_root ) 
