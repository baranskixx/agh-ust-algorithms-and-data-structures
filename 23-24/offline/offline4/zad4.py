from zad4testy import runtests


def switch_list(G):
  V = max(G, key = lambda x: x[1])[1] + 1
  P = [[] for _ in range(V)]
  for point in G:
    u, v, p = point
    P[u].append((v, p))
    P[v].append((u, p))
  return P


def Flight(L,x,y,t):
  G = switch_list(L)
  T = [False] * len(G)

  def dfs(u, Mini, Maxi):
    if Mini <= Maxi:
        if u == y:
            return True
        
        T[u] = True
        # print(u, Mini, Maxi) 
        for s, p in G[u]:
            if not T[s]:
                if dfs(s, max(Mini, p-t), min(Maxi, p+t)):
                    return True
                T[s] = False
        return False
  return dfs(x, float('-inf'), float('inf'))

# L = [(0,1,2000), (0,2,2100), (1,3,2050), (2,3,2300), (2,5,2300), (3,4,2400), (3,5,1990), (4,6,2500), (5,6,2100)]

# print(switch_list(L))

# print(Flight(L,0,6,60))

            
runtests( Flight, all_tests = True )