from zad1testy import runtests

INF = 1e9

def calculate_capacity(X):
    return X[0] * (X[2] - X[1])

def select_buildings(T, p):
    n = len(T)
    T = [[x[0], x[1], x[2], x[3], i] for i, x in enumerate(T)]

    T = sorted(T, key= lambda x : x[1])
    T = sorted(T, key= lambda x : x[2])
    PREV = [-1] * n

    for x in range(1, n):
        for y in range(x-1, -1, -1):
            if T[y][2] < T[x][1]:
                PREV[x] = y
                break
    
    S = [0] * n
    C = [INF] * n
    R = [None for _ in range(n)]

    for x in range(n):
        capacity = calculate_capacity(T[x])
        prev_capacity = 0 if PREV[x] == -1 else S[PREV[x]]
        prev_cost = 0 if PREV[x] == -1 else C[PREV[x]]
        if x == n-1:
            print(capacity)
            print(prev_capacity)
            print(prev_cost)
        if S[x-1] > capacity + prev_capacity:
            S[x] = S[x-1]
            C[x] = C[x-1]
            R[x] = R[x-1]
        elif S[x-1] == capacity + prev_capacity:
            S[x] = capacity + prev_capacity
            if T[x][3] + prev_cost < C[x-1]:
                C[x] = T[x][3] + prev_cost
                R[x] = [T[x][-1]] if PREV[x] == -1 else [T[x][-1]] + R[PREV[x]]
            else:
                C[x] = C[x-1]
                R[x] = R[x-1]
        else:
            S[x] = capacity + prev_capacity
            C[x] = T[x][3] + prev_cost
            R[x] = [T[x][-1]] if PREV[x] == -1 else R[PREV[x]] + [T[x][-1]]
    print(S)
    print(PREV)
    return sorted(R[-1])


runtests( select_buildings ) 
