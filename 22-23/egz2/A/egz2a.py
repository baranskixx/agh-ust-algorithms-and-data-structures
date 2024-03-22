from egz2atesty import runtests

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
