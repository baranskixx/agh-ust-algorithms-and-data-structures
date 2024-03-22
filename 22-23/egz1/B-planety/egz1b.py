from egz1btesty import runtests
"""
Autor rozwiazania: Adam Barański
Złozonosc czasowa: O(n * E)
Złozonosc pamieciowa: O(n * E)

Idea:
Zgodnie z podpowiedzia do zadania korzystamu z funkcji F(i, e) ktora oznacza minimalny
Koszt na dostanie sie na planete, ktorej dane znajduja sie pod indeksem i majac w baku e energii
"""


INF = 1e12

def planets( D, C, T, E ):
    n = len(D)

    F = [[INF] * (E + 1) for _ in range(n)]

    tp_0_x, tp_0_cost = T[0]
    F[tp_0_x][0] = tp_0_cost
    for fuel in range(E):
        F[0][fuel] = C[0] * fuel

    for i in range(1, n):
        dist_diff = D[i] - D[i-1]
        for e in range(E+1):
            if e + dist_diff < E+1:
                F[i][e] = min(F[i][e], F[i-1][e + dist_diff])
            F[i][e] = min(F[i][e], F[i][e-1] + C[i])
        tp_dest, tp_cost = T[i]
        if tp_dest != i:
            F[tp_dest][0] = min(F[tp_dest][0], F[i][0] + tp_cost)

    return min(F[n-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
