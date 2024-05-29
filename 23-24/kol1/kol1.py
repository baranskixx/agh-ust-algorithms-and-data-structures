from kol1testy import runtests

INF = 1e9

def left_child_index(i):
  return 2 * i + 1

def right_child_index(i):
  return 2 * i + 2

def parent_index(i):
  return (i-1) // 2

def heapify(A, n, i):
    left_index = left_child_index(i)
    right_index = right_child_index(i)
    max_index = i

    if left_index < n and(A[left_index][0] > A[max_index][0] or (A[left_index][0] == A[max_index][0] and A[left_index][1] < A[max_index][1])):
       max_index = left_index
    if right_index < n and (A[right_index][0] > A[max_index][0] or (A[right_index][0] == A[max_index][0] and A[right_index][1] < A[max_index][1])):
       max_index = right_index

    if max_index != i:
       A[i], A[max_index] = A[max_index], A[i]
       heapify(A, n, max_index)

def build_heap(A):
    n = len(A)
    for i in range(parent_index(n-1), -1, -1):
       heapify(A, n, i)

def maxrank(T):
    n = len(T)
    T = [(x, i) for i, x in enumerate(T)]
    build_heap(T)
    max_val = -1

    for i in range(n):
        elem = T[0]
        T[0], T[n-i-1] = T[n-i-1], T[0]
        T[n-i-1] = (-INF, -INF)
        heapify(T, n, 0)
        if max_val <= elem[1] - i:
           max_val = elem[1] - i
    
    return max_val
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
