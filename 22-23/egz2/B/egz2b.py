from egz2btesty import runtests

"""
Autor rozwiązania: Adam Barański

f(i,j) = minimalna suma odległości biurowców z pozycji X[0],...,X[i] do przydzielonych im
działek z pozycji X[0], ..., X[j]
"""

INF = 1e9

def parking(X,Y):
  n, m = len(X), len(Y)

  F = [[INF] * m for _ in range(n)]

  for i in range(m):
    F[0][i] = min(abs(X[0] - Y[i]), F[0][i-1])

  for i in range(1, n):
    for j in range(1, m):
      F[i][j] = min(F[i][j-1], abs(X[i] - Y[j]) + F[i-1][j-1])
      
  return min(F[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
