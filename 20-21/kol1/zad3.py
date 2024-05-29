from zad3testy import runtests

"""
Autor rozwiązania : Adam Barański
Złożoność obliczeniowa: O(n)

Sortujemy zwyczajne sortowanie kubełkowe, przyjmując jako nasz obszar [0, max(P[1])]
"""

# [4, 2, 7, 1]

# L = [4, 2]
# R = [7, 1]

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

def bucket_sort(T, max_value):
    n = len(T)

    buckets = [[] for _ in range(n)]
    width = max_value / n

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

def SortTab(T,P):
    max_value = max(P, key= lambda x : x[1])[1]
    bucket_sort(T, max_value)
    return
runtests( SortTab )