from egz1btesty import runtests

"""
Autor rozwiązania: Adam Barański

Złożoność obliczeniowa: O(nk) 
Idea:
F[i][x] - maksymalna wartosc ciagu jaka mozemy uzyskac z dowolnego spojnego podciagu w tablicy
zawierajacego element i po usunieciu dokladnie x elementow
"""
  

INF = 1e9

def kstrong( T, k):
  n = len(T)
  F = [[-INF] * (k+1) for _ in range(n)]
  F[0][0] = T[0]
  
  for i in range(1, n):
    for x in range(k+1):
      if x > 0:
        F[i][x] = max(T[i], F[i-1][x] + T[i], F[i-1][x-1])
      else:
        F[i][x] = max(T[i], F[i-1][x] + T[i])
  return max([max(row) for row in F])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
