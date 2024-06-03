from zad2testy import runtests

"""
Autor rozwiązania: Adam Barański
Zlozonosc obliczeniowa: O(n^2)

Co tu pisac jak tu widac wszystko
"""

def tower(A):
    n = len(A)
    F = [1] * n

    for x in range(1, n):
        for y in range(x-1, -1, -1):
            if A[x][0] >= A[y][0] and A[x][1] <= A[y][1]:
                F[x] = max(F[x], F[y] + 1)
    return max(F)

runtests(tower)
