from zad1testy import runtests

INF = 1e9

def calculate_capacity(X):
    return X[0] * (X[2] - X[1])

def select_buildings(T, p):
    n = len(T)
    T = [[x[0], x[1], x[2], x[3], i] for i, x in enumerate(T)]

    T = sorted(T, key= lambda x : x[2], reverse=True)
    T = sorted(T, key= lambda x : x[1])
    PREV = [-1]*n

    for x in range(1, n):
        for y in range(x-1, -1, -1):
            if T[y][2] < T[x][1]:
                PREV[x] = y
                break
    
    S = [0] * n
    C = [INF] * n

    for x in range(n):
        capacity = calculate_capacity(T[x])
        if PREV[x] == -1:
            if S[x-1] > capacity:
                S[x] = S[x-1]
                C[x] = C[x-1]
            elif S[x-1] == capacity:
                S[x] = capacity
                C[x] = min(T[x][3], C[x-1])
            else:
                S[x] = capacity
                C[x] = T[x][3]
        else:
                



    return []

runtests( select_buildings ) 
