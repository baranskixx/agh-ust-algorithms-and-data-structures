from zad3testy import runtests

"""
Autor : Adam Barański
Złożoność obliczeniowa: O( V + E ), gdzie V to ilosc krawedzi w grafie, E ilosc krawedzi 

Idea: 
Budujemy graf skierowany, w oparciu o otrzymana tabele
Istnieje krawedz x -> y wtw gdy x poprzedza y jesli chodzi o wykonanie
Nastepnie na tak utworzonym grafie wykonujemy sortowanie topologiczne i zwracamy tablice, ktora uzyskalismy po posortowaniu
"""

class Vertex:
    def __init__(self, index):
        self.neigh = []
        self.index = index

def create_graph(T):
    n = len(T)
    G = [Vertex(i) for i in range(n)]
    
    for u in range(n):
        for v in range(n):
            if T[u][v] == 1:
                G[u].neigh.append(v)
    
    return G

def top_sort(G):
    n = len(G)
    V = [False] * n
    seq = []
    def dfs(u):
        V[u] = True

        for v in G[u].neigh:
            if not V[v]:
                dfs(v)
        
        seq.append(u)
    
    for u in range(n):
        if not V[u]:
            dfs(u)
    
    return seq[::-1]


def tasks(T):
    G = create_graph(T)
    return top_sort(G)

runtests( tasks )
