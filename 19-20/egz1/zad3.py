from zad3testy import runtests
import math

"""
Autor rozwiązania : Adam Barański
Złożoność obliczeniowa:    O(n)
Złożonośc pamięciowa:      O(n)

Idea:
Korzystamy z bucket sorta po konwersji danych przy użyciu math.log()
Po posortowaniu elementów dokonujemy konwersji by przywrócić dane do ich pierwotnej postaci
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def bucket_sort(T):
    n = len(T)

    buckets = [[] for _ in range(n)]
    width = 1 / n

    for elem in T:
        bucket_index = min(n-1, int(elem // width))
        buckets[bucket_index].append(elem)
    
    for bucket in buckets:
        merge_sort(bucket)

    index = 0
    for bucket in buckets:
        for elem in bucket:
            T[index] = elem
            index += 1
    
    return T


def fast_sort(tab, a):
    tab = [math.log(x, a) for x in tab]
    bucket_sort(tab)
    tab = [a ** x for x in tab]
    return tab



runtests( fast_sort )
