from zad1testy import runtests
from queue import PriorityQueue

"""
Autor rozwiązania : Adam Barański
Złożoność obliczeniowa:    O(E * log V)

Idea:
Zaczynamy od rozmnożenia grafu - każdy wierzchołek dzielimy na 3 jemu odpowiadające
dla i będą to i, n+i, 2 * n + 1
Następnie wykonujemy algorytm Djikstry w oparciu o kolejkę priorytetową i graf reprezentowany w postaci list sąsiedztwa
Zaczynamy z wierzchołkow A, n + A oraz 2 * n + A działamy tak długo jak nie dotrzemy do wierzchołka B, n + B lub 2 * n + B
"""

INF = 1e9

class Vertex():
    def __init__(self):
        self.neighbours = []
    
    def add_neighbour(self, _to, _cost):
        self.neighbours.append((_to, _cost))
    
COST_TO_INDEX_FROM = {
    1 : [1, 2],
    5 : [0, 2],
    8 : [0, 1]
}

COST_TO_INDEX_TO= {
    1 : 0,
    5 : 1,
    8 : 2
}

def islands(G, A, B):
    n = len(G)

    GRAPH = [Vertex() for _ in range(3 * n)]
    for u, neigh in enumerate(G):
        for v, cost in enumerate(neigh):
            if cost == 0:
                continue
            FROM = COST_TO_INDEX_FROM[cost]
            mult_to = COST_TO_INDEX_TO[cost]
            for mult_from in FROM:
                GRAPH[u + n * mult_from].add_neighbour(v + n * mult_to, cost)
    
    Q = PriorityQueue()
    D = [INF] * (3 * n)
    for mult in range(3):
        Q.put((0, A + n * mult))
        print(mult * A)
    
    while not Q.empty():
        d, u = Q.get()

        if u in [B, B + n, B + 2 * n]:
            return d
        
        if D[u] <= d:
            continue

        D[u] = d
        for v, cost in GRAPH[u].neighbours:
            if D[v] > d + cost:
                print(v)
                Q.put((d + cost, v))
        
    return None

runtests( islands ) 
