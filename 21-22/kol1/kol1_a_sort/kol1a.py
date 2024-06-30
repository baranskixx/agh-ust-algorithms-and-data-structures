from kol1atesty import runtests

"""
Autor rozwiazania: Adam Baranski

Złożoność obliczeniowa: O(nk)
Idea:
Kazdy napis zapisujemy jako mniejszy leksykograficznie ze zbioru (napis, palindrom_napisu)
Sortujemy wg dlugosci na bucketu
Sortujemy napisy w obrebie kazdego bucketu
Znajdujemy maksymalny zbior napisow rownowaznych
"""

def split_to_buckets(T):
    max_len = len(max(T, key = lambda x : len(x)))
    
    buckets = [[] for _ in range(max_len + 1)]
    for s in T:
        buckets[len(s)].append(s)
    
    return buckets

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 26  

    for i in range(n):
        index = ord(arr[i][exp]) - ord('a')
        count[index] += 1

    for i in range(1, 26):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = ord(arr[i][exp]) - ord('a')
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return
    
    max_len = len(arr[0])

    for exp in range(max_len-1, -1, -1):
        counting_sort(arr, exp)

def g(T):
    n = len(T)
    for i in range(n):
        palindromes = [T[i], T[i][::-1]]
        radix_sort(palindromes)
        T[i] = palindromes[0]
    
    buckets = split_to_buckets(T)
    result = 0
    for bucket in buckets:
        radix_sort(bucket)
        i = 1
        cnt = 1
        while i < len(bucket):
            if bucket[i] == bucket[i-1]:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 1
            i += 1
        result = max(result, cnt)
    return result


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests(g, all_tests=True)
