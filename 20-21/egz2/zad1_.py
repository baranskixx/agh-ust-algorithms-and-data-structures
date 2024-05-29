from zad1testy import runtests
# 
# u, v
# d(s,t)
# 1 + d(s, u) + d(t, v) == d(s,t) or 1 + d(s, v) + (t, u) == d(s,t)
# d(s, u), d(s, t)
# 


# O (N^2)
def create_graph(I):
    n = len(I)

    G = [[] for _ in range(n)]
    for x in range(n-1):
        for y in range(x+1, n):
            a, b = I[x]
            c, d = I[y]

            if b == c:
                G[x].append(y)
            if a == d:
                G[y].append(x)
    
    return G

def dfs(I, G, x, y):
    R = [False] * len(G)
    def rek(u):
        if I[u][1] == y:
            R[u] = True
            return True
        
        for v in G[u]:
            if R[v] or rek(v):
                R[u] = True
        return R[u]

    for u in range(len(G)):
        if I[u][0] == x:
            rek(u)
    
    result = []
    for i in range(len(G)):
        if R[i]:
            result.append(i)
    
    return result
    

def intuse( I, x, y ):
    n = len(I)
    G = create_graph(I)

    return dfs(I, G, x, y)

    
runtests( intuse )


