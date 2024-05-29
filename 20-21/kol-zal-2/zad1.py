from zad1testy import runtests

"""
Autor rozwiazania: Adam Baranski

Złożoność obliczeniowa: O(N)
Złożonośc pamięciowa: O(N)
Idea:
Tworzymy tablicę L i R, odpowiadające iloczynowi prostokątów od 0 do i (L) lub od i do konca (R)
Nastepnie z uzyciem obu tych tablic sprawdzamy iloczyn sasiadow kazdego elementu 
(odpowiada to usunieciu tego konkretnego elementu)
"""

INF = 1e12


def intersection(A, B):
    if A is None or B is None:
        return None

    x1 = max(A[0], B[0])
    y1 = max(A[1], B[1])
    x2 = min(A[2], B[2])
    y2 = min(A[3], B[3])

    if x1 < x2 and y1 < y2:
        return (x1, y1, x2, y2)
    else:
        return None


def rectangle_area(rect):
    if rect is None:
        return 0

    width = rect[2] - rect[0]
    height = rect[3] - rect[1]

    return width * height


def rect(D):
    n = len(D)

    L = [None] * n
    R = [None] * n

    for i in range(n):
        L[i] = D[i]
        if i > 0:
            L[i] = intersection(L[i], L[i-1])
    
    for i in range(n-1, -1, -1):
        R[i] = D[i]
        if i < n-1:
            R[i] = intersection(R[i], R[i+1])
    
    max_area = 0
    max_index = 0
    if rectangle_area(L[n-2]) > rectangle_area(R[1]):
        max_index = n-1
        max_area = rectangle_area(L[n-2])
    else:
        max_index = 0
        max_area = rectangle_area(R[1])
    
    for i in range(1, n-1):
        area = rectangle_area(intersection(L[i-1], R[i+1]))
        if area > max_area:
            max_area = area
            max_index = i
    
    return max_index


    
runtests( rect )


