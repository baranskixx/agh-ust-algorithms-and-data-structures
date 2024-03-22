from egz3atesty import runtests
from queue import PriorityQueue

"""
Autor rozwiazania: Adam Baranski

Zlozonosc obliczeniowa: O(n^2)
Zlozonosc pamieciowa : O(n)

Idea:
Stosujemy algorytm Dijkstry na macierzy z dodatkowym parametrem, iloscia pozostalych godzin,
jakie pozostaly nam nim bedziemy musieli przenocowac w jakims zamku
Do innej krawedzi mozemy przejsc jesli pozwoli nam to dozwolony czas przed pojsciem spac
Przy kazdym wierzcholku stosujemy rowniez sytuacje, w której idziemy spać w danym zamku
i dopiero potem sprawdzamy (juz z pelnym limitem godzin) czy mozemy przejsc do bezposrednio polaczonego wierzcholka
"""

INF = 1e12

def goodknight(G, s, t):
    n = len(G)
    Q = PriorityQueue()
    D = [INF] * n

    Q.put((0, (16, s)))

    while not Q.empty():
        d, data = Q.get()
        left_h, u = data

        if D[u] < d:
            continue
        
        D[u] = d
        for v, cost in enumerate(G[u]):
            if cost == -1:
                continue
            elif cost <= left_h and d + cost < D[v]:
                Q.put((d + cost, (left_h - cost, v)))

        left_h = 16
        d += 8

        for v, cost in enumerate(G[u]):
            if cost == -1:
                continue
            elif cost <= left_h and d + cost < D[v]:
                Q.put((d + cost, (left_h - cost, v)))
    return D[t]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )