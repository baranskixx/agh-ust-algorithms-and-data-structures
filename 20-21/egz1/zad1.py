from zad1testy import runtests

"""
Autor rozwiązania : Adam Barański
Złożoność obliczeniowa:    O(n*logn)

Idea:
Uzywajac stabilnego sortowania (merge sort) sortujemy 
liste, uprzednio dodajac do kazdego elementu pierwotny indeks tego elementu przed posortowaniem

W ten sposob uzyskujemy rozwiazanie biorac maksymalna roznice miedzy 
indeksem kazdego elementu przed i po posortowaniu
"""

def merge_sort(A, index):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        merge_sort(L, index)
        merge_sort(R, index)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][index] < R[j][index]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

def chaos_index( T ):
    n = len(T)
    T = [(x, i) for i, x in enumerate(T)]
    merge_sort(T, 0)

    max_res = 0
    for i in range(n):
        max_res = max(max_res, abs(i - T[i][1]))
    print(T)
    return max_res


runtests( chaos_index )
