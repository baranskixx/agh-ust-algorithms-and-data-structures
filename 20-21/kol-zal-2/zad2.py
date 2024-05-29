from zad2testy import runtests

"""
Autor rozwiazania: Adam Baranski

Złożoność obliczeniowa: O(N + M)
Złozonosc pamieciowa: O(10^K)
Idea:
Tworzymy graf w oparciu o warunek podany w zadaniu, sortujemy topologiczne.
"""

def topological_sort(graph):
    def dfs(v):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)
        topological_stack.append(v)

    n = len(graph)
    visited = [False] * n
    topological_stack = []

    for vertex in range(n):
        if not visited[vertex]:
            dfs(vertex)

    return topological_stack[::-1]

def order(L,K):
    n = len(L)

    B = [[] for _ in range(10 ** K)]
    for i, num in enumerate(L):
        bucket_index = num // (10 ** K)
        if bucket_index < 10 ** K:
            B[bucket_index].append(i)
    
    G = [None] * n
    for i, num in enumerate(L):
        bucket_index = num % (10 ** K)
        G[i] = B[bucket_index]
    
    result_index = topological_sort(G)
    return [L[result_index[x]] for x in range(n)]


runtests( order )


