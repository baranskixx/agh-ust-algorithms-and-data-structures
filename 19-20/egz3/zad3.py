from zad3testy import runtests
from zad3testy import Node

"""
Autor rozwiązania: Adam Barański
Korzystamy z kopca do przechowywania list, z jego uzyciem wyciagamy najmniejszy dostepny element
"""

def left_child_index(i):
  return 2 * i + 1

def right_child_index(i):
  return 2 * i + 2

def parent_index(i):
  return (i-1) // 2

def heapify(A, n, i):
    left_index = left_child_index(i)
    right_index = right_child_index(i)
    min_index = i

    if left_index < n and A[left_index].val < A[min_index].val:
       min_index = left_index
    if right_index < n and A[right_index].val < A[min_index].val:
       min_index = right_index

    if min_index != i:
       A[i], A[min_index] = A[min_index], A[i]
       heapify(A, n, min_index)

def build_heap(A):
    n = len(A)
    for i in range(parent_index(n-1), -1, -1):
       heapify(A, n, i)
    
def merge_lists(T):
    n = len(T)
    
    heap = []
    for i in range(n):
        heap.append(T[i])
        T[i] = T[i].next
    
    build_heap(T)
    start = Node(None)
    p = start
    
    while heap[0].val != 1e9:
        node = heap[0]
        heap[0] = heap[0].next if heap[0].next is not None else Node(1e9)
        heapify(heap, n, 0)
        node.next = None
        p.next = node
        p = p.next
    
    return start.next


runtests( merge_lists )
