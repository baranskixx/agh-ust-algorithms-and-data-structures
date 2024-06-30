from zad1testy import runtests
from collections import deque
from bisect import bisect_left

def find_LDS(nums):
    n = len(nums)
    F = [1] * n
    
    for x in range(1, n):
        for y in range(x-1, -1, -1):
            if nums[x] < nums[y]:
                F[x] = max(F[x], F[y] + 1)
    
    return F

def find_LIS(nums):
    n = len(nums)
    F = [1] * n
    
    for x in range(n-2, -1, -1):
        for y in range(x+1, n):
            if nums[x] < nums[y]:
                F[x] = max(F[x], F[y] + 1)
    
    return F 

def mr(X):
    n = len(X)
    LIS = find_LIS(X)
    LDS = find_LDS(X)
    
    index = -1
    res = -1
    for i in range(n):
        current_res = LIS[i] + LDS[i] - 1
        if current_res > res:
            res = current_res
            index = i
    
    RES = [X[index]]
    i = index
    j = i - 1
    
    print(LIS, LDS, index)
    while LDS[i] != 1:
        if X[i] < X[j] and LDS[j] == LDS[i] - 1:
            RES.append(X[j])
            i = j
        j -= 1
        
    RES.reverse()
    i = index
    j = i + 1
    
    while LIS[i] != 1:
        if X[i] < X[j] and LIS[j] == LIS[i] - 1:
            RES.append(X[j])
            i = j
        j += 1
    
    return RES
    
runtests( mr )


