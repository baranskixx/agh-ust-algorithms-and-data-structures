from egz2atesty import runtests

"""
Autor rozwiązania: Adam Barański

Złożoność obliczeniowa: O(V + E) 
Idea:
Rozszerzamy graf -> z kazdego wierzcholka robimy 16 (w zaleznosci od ilosci godzin, ktore mozemy
jeszcze podrozowac bez spania)
Korzystamy z faktu, ze krawedzie sa dlugosci maksymalnie 16, i korzystajac z BFS uruchamiamy 
wyszukiwanie najkrotszej sciezki
"""

def dominance(P):
  n = len(P)
  pref_x = [0] * (n + 1)
  pref_y = [0] * (n + 1)

  for x, y in P:
    pref_y[y] += 1
    pref_x[x] += 1
  
  for i in range(1,n+1):
    pref_x[i] += pref_x[i-1]
    pref_y[i] += pref_y[i-1]

  result = 0
  for x, y in P:
     s = pref_x[x-1] + pref_y[y-1] - n + 1
     result = max(result, s)

  return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
