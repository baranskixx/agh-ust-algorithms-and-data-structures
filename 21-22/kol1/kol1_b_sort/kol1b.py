from kol1btesty import runtests

def split_to_buckets(T):
    max_len = len(max(T, key = lambda x : len(x)))
    
    buckets = [[] for _ in range(max_len + 1)]
    for s in T:
        buckets[len(s)].append(s)
    
    return buckets

def sort_string(s):
    count = [0] * 26

    for char in s:
        index = ord(char) - ord('a')  
        count[index] += 1

    sorted_str = ''
    for i in range(26):  
        sorted_str += (chr(i + ord('a')) * count[i])

    return sorted_str

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

def f(T):
    buckets = split_to_buckets(T)
    result = 0
    for bucket in buckets:
        bucket = [sort_string(s) for s in bucket]
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
runtests( f, all_tests=True )
