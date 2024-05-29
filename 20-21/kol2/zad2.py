from zad2testy import runtests
from collections import deque, defaultdict
"""
Autor rozwiązania: Adam Barański

Złożoność obliczeniowa: O(V + E) 
Złożoność pamięciowa: O(V + E)
Idea:
Algorytm skupia się na wyznaczaniu najkrótszej ścieżki między dwoma wierzchołkami (s i t) 
za pomocą algorytmu BFS, który jest wykonywany dwukrotnie z różnych wierzchołków. 
Następnie tworzony jest graf składający się wyłącznie z krawędzi znajdujących się na 
najkrótszej ścieżce między tymi punktami. Wykorzystujemy algorytm Tarjana do znajdowania 
mostów w tym grafie, co pozwala określić, które krawędzie są krytyczne dla zachowania 
najkrótszej ścieżki.
"""


def bfs(graph, start):
    n = len(graph)
    distances = [-1] * n
    queue = deque([start])
    distances[start] = 0
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return distances

def build_shortest_path_graph(G, s, t, dist_s, dist_t):
    shortest_path_graph = defaultdict(list)
    for u in range(len(G)):
        for v in G[u]:
            if u < v:
                if (dist_s[u] + 1 + dist_t[v] == dist_s[t] or
                    dist_s[v] + 1 + dist_t[u] == dist_s[t]):
                    shortest_path_graph[u].append(v)
                    shortest_path_graph[v].append(u)
    return shortest_path_graph

def tarjan_find_bridges(graph, n):
    ids = [-1] * n
    low = [-1] * n
    visited = [False] * n
    bridges = []
    
    def dfs(at, parent, bridges, id_counter):
        visited[at] = True
        low[at] = ids[at] = id_counter[0]
        id_counter[0] += 1
        for to in graph[at]:
            if to == parent:
                continue
            if not visited[to]:
                dfs(to, at, bridges, id_counter)
                low[at] = min(low[at], low[to])
                if ids[at] < low[to]:
                    bridges.append((at, to))
            else:
                low[at] = min(low[at], ids[to])
    
    for i in range(n):
        if not visited[i]:
            dfs(i, -1, bridges, [0])
    
    return bridges

def enlarge(G, s, t):
    dist_s = bfs(G, s)
    dist_t = bfs(G, t)
    if dist_s[t] == -1:
        return None
    
    shortest_path_graph = build_shortest_path_graph(G, s, t, dist_s, dist_t)
    bridges = tarjan_find_bridges(shortest_path_graph, len(G))
    
    if bridges:
        return bridges[0]
    return None

runtests( enlarge ) 
