from kolutesty import runtests

def projects(n, L):
  D = [-1] * n
  G = [[] for _ in range(n)]
  for u, v in L:
    G[v].append(u)
  
  def dfs(u):
    D[u] = 1
    
    for v in G[u]:
      if D[v] == -1:
        dfs(v)
      D[u] = max(D[u], D[v] + 1)
    
  for u in range(n):
    if D[u] == -1:
      dfs(u)
  
  return max(D)
    
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )
