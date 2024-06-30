from zad1testy import runtests

"""
Autor rozwiązania: Adam Barański

Złożoność obliczeniowa: O(n^2) 
Idea:
Problem plecakowy przy dodatkowym uwzglednieniu polozenia akademikow
Aby zrobic w nlogn trzeba szukac preva z uzyciem binary search
"""

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
    
    F = [[0] * (p+1) for _ in range(n)]
    for x in range(T[0][3], p+1):
        F[0][x] = T[0][0] * (T[0][2] - T[0][1])
    
    for i in range(1, n):
        for x in range(p+1):
            F[i][x] = F[i-1][x]
            i_cost = T[i][3]
            i_capacity = T[i][0] * (T[i][2] - T[i][1])
            if i_cost <= x:
                if PREV[i] == -1:
                    F[i][x] = max(F[i][x], i_capacity)
                else:
                    prev_capacity = F[PREV[i]][x - i_cost]
                    F[i][x] = max(F[i][x], i_capacity + prev_capacity)
    
    RES = []
    i = n-1
    x = p
    
    while i != -1 and F[i][x] != 0:
        if F[i][x] == F[i][x-1]:
            x -= 1
        else:
            if F[i][x] == F[PREV[i]][x-T[i][3]] + T[i][0] * (T[i][2] - T[i][1]):
                RES.append(T[i][4])
                x -= T[i][3]
                i = PREV[i]
            else:
                i -= 1
    
    return sorted(RES)
            
            
                


runtests( select_buildings ) 
