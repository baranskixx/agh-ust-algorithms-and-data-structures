from kol3testy import runtests

"""
Autor rozwiazania: Adam Barański
Złozonosc czasowa: O(n ^ 2)

Idea:
F[i][x] - minimalna ilosc drzew, ktore nalezy uciac zeby miec w sadzie ilosc owocow f,
gdzie f % m == x, wybierajac ze zbioru drzew {0, 1, ..., i}
"""

INF = 1e9
def orchard(T, m):
    n = len(T)
    T = [x % m for x in T]
    
    F = [[INF] * m for _ in range(n)]
    F[0][0] = 1
    F[0][T[0]] = 0
    
    for i in range(1, n):
        for x in range(m):
            on_tree = T[i]
            prev_x = x - on_tree 
            F[i][x] = min(F[i-1][prev_x], F[i-1][x] + 1)
    
    return F[-1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
