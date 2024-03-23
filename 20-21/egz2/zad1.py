from zad1testy import runtests

def binary_search(arr, target, index):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid][index] == target:
            result = mid
            right = mid - 1
        elif arr[mid][index] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def intuse( I, x, y ):
    n = len(I)
    I = [(x[0], x[1], i) for i, x in enumerate(I)]
    
    I = sorted(I, key = lambda x : x[0])
    F = [False] * n
    for a, b, i in I:
        if a == x:
            F[i] = True
    
    for a, b, i in I:
        if not F[i]:
            continue
        neigh_i = binary_search(I, b, 0)
        if neigh_i == -1:
            continue
        while neigh_i < n and b == I[neigh_i][0]:
            F[I[neigh_i][2]] = True
            neigh_i += 1
    
    I = sorted(I, key = lambda x : x[1])
    B = [False] * n
    for a, b, i in reversed(I):
        if b == y:
            B[i] = True
    
    for a, b, i in reversed(I):
        if not B[i]:
            continue
        neigh_i = binary_search(I, a, 1)
        if neigh_i == -1:
            continue
        while neigh_i < n and a == I[neigh_i][1]:
            B[I[neigh_i][2]] = True
            neigh_i += 1
    
    ans = []
    for i in range(n):
        if F[i] and B[i]:
            ans.append(i)

    return ans

    
runtests( intuse )


