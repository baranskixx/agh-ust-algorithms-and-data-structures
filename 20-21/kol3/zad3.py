from zad3testy import runtests
from zad3EK    import edmonds_karp

def floyd_warshall(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            if T[i][j] == 0:
                T[i][j] = 1e10

    for i in range(n):
        for j in range(n):
            for k in range(n):
                T[i][j] = min(T[i][j], T[i][k] + T[k][j])


def BlueAndGreen(T, K, D):
    n = len(T)
    floyd_warshall(T)

    G = [[0] * (n+2) for _ in range(n+2)]
    for i in range(n):
        if K[i] == 'B':
            G[n][i] = 1
            for u in range(n):
                if K[i] != K[u] and T[i][u] >= D:
                    G[i][u] = 1
        else:
            G[i][n+1] = 1
    
    return edmonds_karp(G, n, n+1)

runtests( BlueAndGreen ) 
