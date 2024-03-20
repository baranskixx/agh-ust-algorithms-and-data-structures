from zad1testy import runtests

"""
Autor : Adam Barański
Złożoność obliczeniowa: O(n * E)

Idea: 
Tworzymy F(i, x) gdzie funkcja ta oznacza minimalny koszt (ilosc skokow) 
Konieczny by dostac sie na pole 'i' z 'x' energii
"""

INF = 1e9

def zbigniew(A):
    n = len(A)
    max_energy = sum(A)
    start_energy = A[0]

    F = [[INF] * (max_energy + 1) for _ in range(n)]
    F[0][start_energy] = 0

    for i in range(n):
        for e in range(1, max_energy):
            if F[i][e] != INF:
                for x in range(1, e + 1):
                    if i + x >= n:
                        break
                    F[i + x][e - x + A[i + x]] = min(F[i + x][e - x + A[i + x]], F[i][e] + 1)
    result = min(F[n-1])
    return result if result != INF else -1
       

runtests( zbigniew ) 
