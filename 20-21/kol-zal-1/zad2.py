from zad2testy import runtests

"""
Autor rozwiazania: Adam Baranski

Złozonosc obliczeniowa:
Zlozonosc pamieciowa: 

1.  Szukamy wszystkich punktów artykulacji grafu.
2.  Dla kazdego znalezionego punktu artykulacji zaczynamy odpalac z niego DFS
    Ilość wierzchołków, do których bezpośrednio przejdziemy z danego punktu artykulacji jest iloscia rozlacznych czesci na jakie rozdzieli sie graf po usunieciu tego punktu artykulacji
3.  Zwracamy wierzcholek o maksymalnej ilosci sasiadow, do których przeszlismy z niego
"""

def breaking(G):
    n = len(G)
    discovery = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    articulation_points = [False] * n
    time = [0]  # Wrapper for integer
    
    # Helper function to perform DFS
    def dfs(u):
        nonlocal time
        children = 0
        discovery[u] = low[u] = time[0]
        time[0] += 1
        
        for v in range(n):
            if G[u][v] > 0:  # There is a connection
                if discovery[v] == -1:  # v is not visited
                    parent[v] = u
                    children += 1
                    dfs(v)
                    
                    # Check if the subtree rooted at v has a connection back to one of the ancestors of u
                    low[u] = min(low[u], low[v])
                    
                    # (1) u is root of DFS tree and has two or more children.
                    # (2) u is not root and low value of one of its child is more than discovery value of u.
                    if (parent[u] == -1 and children > 1) or (parent[u] != -1 and low[v] >= discovery[u]):
                        articulation_points[u] = True
                elif v != parent[u]:  # Update low value of u for parent function calls.
                    low[u] = min(low[u], discovery[v])
    
    # Find all articulation points
    for i in range(n):
        if discovery[i] == -1:
            dfs(i)
    
    # Function to count components formed by removing a point
    def count_components_excluding(exclude):
        visited = [False] * n
        def dfs_count(v):
            stack = [v]
            while stack:
                node = stack.pop()
                for w in range(n):
                    if G[node][w] > 0 and not visited[w] and w != exclude:
                        visited[w] = True
                        stack.append(w)
        
        count = 0
        for i in range(n):
            if i != exclude and not visited[i]:
                visited[i] = True
                dfs_count(i)
                count += 1
        return count
    
    # Determine which articulation point maximizes the number of components
    max_components = 0
    best_vertex = None
    for i in range(n):
        if articulation_points[i]:
            components = count_components_excluding(i)
            if components > max_components:
                max_components = components
                best_vertex = i
    
    return best_vertex


runtests( breaking )