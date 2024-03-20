from zad2testy import runtests

"""
Autor rozwiązania : Adam Barański
Złożoność obliczeniowa: O(n * log(k))

Tworzymy tablicę rozmiaru (k+1), wrzucamy do niej pierwsze k+1 elementów listy i 
tworzymy w tablicy strukturę kopca
Następnie (tak długo jak nie skończą nam się elementy w oryginalnej liście) zamieniamy minimalny element kopca z kolejnym z nieposortowanej listy
Minimalny element ląduje na końcu listy posortowanej 
Następnie, gdy oryginalna lista jest pusta wyciągamy minimalne elementy z kopca opróżniając go
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
    max_index = i

    if left_index < n and A[left_index].val < A[max_index].val:
       max_index = left_index
    if right_index < n and A[right_index].val < A[max_index].val:
       max_index = right_index

    if max_index != i:
       A[i], A[max_index] = A[max_index], A[i]
       heapify(A, n, max_index)

def build_heap(A):
    n = len(A)
    for i in range(parent_index(n-1), -1, -1):
       heapify(A, n, i)

def SortH(p,k):
    if k == 0:
       return p
    heap = [None] * (k+1)

    for i in range(k+1):
        tmp = p
        p = p.next
        tmp.next = None
        heap[i] = tmp
    
    build_heap(heap)

    guardian = Node()
    sorted_list_end = guardian

    print('x')
    while p != None:
        prev = p
        p = p.next
        prev.next = None
        prev, heap[0] = heap[0], prev
        sorted_list_end.next = prev
        sorted_list_end = sorted_list_end.next
        heapify(heap, k+1, 0)
    
    for heap_size in range(k+1, 0, -1):
       heap[0], heap[heap_size-1] = heap[heap_size-1], heap[0]
       sorted_list_end.next = heap[heap_size-1]
       heapify(heap, heap_size, 0)
       sorted_list_end = sorted_list_end.next
    print(heap[0].val)
    
    sorted_list_end.next = None
    return guardian.next

runtests( SortH ) 