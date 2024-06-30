from egz1atesty import runtests
from queue import PriorityQueue
from math import floor
  
"""
Autor rozwiązania: Adam Barański

Złożoność obliczeniowa: O(V * log(E)) 
Idea:
1. Diikstra z s do kazdego wierzcholka
2. Dijkstra z t do kazdego wierzcholka
"""
  
INF = 1e9

def dijkstra(G, s):
  D = [INF] * len(G)
  Q = PriorityQueue()
  
  Q.put((0, s))
  
  while not Q.empty():
    d, v = Q.get()
    
    if d >= D[v]:
      continue
    D[v] = d
    
    for u, dist_to_u in G[v]:
      if d + dist_to_u < D[u]:
        Q.put((d + dist_to_u, u))
    
  return D

def armstrong( B, G, s, t):
  n = len(G)
  
  GRAPH = [[] for _ in range(n)]
  for u, v, d in G:
    GRAPH[u].append((v, d))
    GRAPH[v].append((u, d))
  
  Ds = dijkstra(GRAPH, s)
  Dt = dijkstra(GRAPH, t)
  
  result = Ds[t]
  
  for u, p, q in B:
    result = min(result, Ds[u] + Dt[u] * (p/q))
  return floor(result)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
