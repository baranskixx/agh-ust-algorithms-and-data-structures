from zad3testy import runtests
"""
Autor: Adam Barański

Rozwiązanie akceptowalne
Złożoność obliczeniowa: O (n^2)
Złożoność pamięciowa: O(n)

W tablicy D zapisujemy dla każdemu punktu ilosc punktów które dominuje
Zawartość tej tablicy wyznaczamy w O(n^2)
Następnie zwracamy maksimum z tablicy D.
"""
def dominance_n2(P):
    n = len(P)

    P = sorted(P, key = lambda x : x[1])
    P = sorted(P, key = lambda x : x[0])
    D = [0] * n

    for x in range(n-1):
        for y in range(x+1, n):
            if P[y][0] > P[x][0] and P[y][1] > P[x][1]:
                D[y] += 1
    
    return max(D)
    

def count_sort(arr, index):
    max_val = max(arr, key = lambda x : x[index])
    count_arr = [0] * (max_val + 1)
    output_arr = [0] * len(arr)

    for num in arr:
        count_arr[num[index]] += 1

    for i in range(1, max_val + 1):
        count_arr[i] += count_arr[i - 1]

    for num in reversed(arr):
        output_arr[count_arr[num[index]] - 1] = num
        count_arr[num[index]] -= 1

    return output_arr

"""
Autor: Adam Barański

Rozwiązanie akceptowalne
Złożoność obliczeniowa: O (n)
Złożoność pamięciowa: O(n)

W tablicy D zapisujemy dla każdemu punktu ilosc punktów które dominuje
Zawartość tej tablicy wyznaczamy w O(n^2)
Następnie zwracamy maksimum z tablicy D.
"""

def count_sort(arr, idx):
    max_val = max(arr, key=lambda x: x[idx])[idx]
    count_arr = [0] * (max_val + 1)
    output_arr = [0] * len(arr)

    for num in arr:
        count_arr[num[idx]] += 1

    for i in range(1, max_val + 1):
        count_arr[i] += count_arr[i - 1]

    for num in reversed(arr):
        output_arr[count_arr[num[idx]] - 1] = num
        count_arr[num[idx]] -= 1

    return output_arr

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

