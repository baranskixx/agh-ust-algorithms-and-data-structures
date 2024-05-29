from zad2testy import runtests
from math import ceil, sqrt
from queue import PriorityQueue

"""
Autor : Adam Barański
Złożoność obliczeniowa: O( E * logV ) 

Idea: 
Korzystamy z algorytmu Kruskala, operujemy na liscie posortowanych krawedzi, biorac jako "pierwsza" krawedz
kolejna krawedz z tablicy przy kazdej iteracji - tym sposobem sprawdzamy wszystkie mozliwe efektywne mozliwosci zbudowania autostrat
Algorytm Kruskala zawsze wybierze nam najmniejsze mozliwe krawedzie, nas interesuje znalezienie takich, w których roznica odległości
najmniejszej i najwiekszej krawedzi sa minimalne 
"""
class Node:
    def __init__(self):
        self.rank = 0
        self.parent = self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent    

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: return
    if x.rank > y.rank: 
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank: y.rank += 1

def distance(X, Y):
    return ceil(sqrt((X[0] - Y[0]) ** 2 + (X[1] - Y[1]) ** 2))

def highway(A):
    n = len(A)
    E = []

    for x in range(n):
        for y in range(x+1, n):
            if y != x:
                dist = distance(A[x], A[y])
                E.append((dist, x, y))
        
    E = sorted(E, key = lambda x : x[0])
    m = len(E)
    result = 1e10

    for i in range(m):
        V = [Node() for _ in range(n)]
        D = []

        for j in range(i, m):
            d = E[j][0]
            x = V[E[j][1]]
            y = V[E[j][2]]
            if find(x) != find(y):
                union(x, y)
                D.append(d)
    
        if len(D) == n-1:
            result  = min(result, D[-1] - D[0])
    
    return result
        

runtests( highway ) 
