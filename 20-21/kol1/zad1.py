from zad1testy import runtests


"""
Autor rozwiązania : Adam Barański
Złożoność obliczeniowa: O(n^2)
Złożonośc pamięciowa: O(n^2)

Robimy quickselect na tablicy 2D
Mapujemy "zwykle", jednowymiarowe indeksy na te na macierzy w następujący sposób
1. Pierwsze pola zajmują elementy, które w wyniku posortowania znajdą się pod przekątną
2. Kolejne te, które wylądują na przekątnej
3. Na końcu te, które lądują na przekątną
"""


def partition(arr, low, high, I):
    high_y, high_x = I[high]
    pivot = arr[high_y][high_x]
    i = low - 1
    for j in range(low, high):
        j_y, j_x = I[j]
        elem = arr[j_y][j_x]
        if elem < pivot:
            i += 1
            i_y, i_x = I[i]
            arr[j_y][j_x], arr[i_y][i_x] = arr[i_y][i_x], arr[j_y][j_x]
    i_y, i_x = I[i+1]
    arr[i_y][i_x], arr[high_y][high_x] = arr[high_y][high_x], arr[i_y][i_x]
    return i + 1

def quickselect(arr, low, high, k, I):
    if low == high:
        low_y, low_x = I[low]
        return arr[low_y][low_x]

    pivot_index = partition(arr, low, high, I)

    if k == pivot_index:
        y, x = I[k]
        return arr[y][x]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k, I)
    else:
        return quickselect(arr, pivot_index + 1, high, k, I)


def Median(T):
    n = len(T)
    I = [None] * (n**2)
    index = 0 

    # indeksy elementow pod przekatna
    for y in range(1, n):
        for x in range(y):
            I[index] = (y, x)
            index += 1
    # indeksy elementow na przekatnej
    start_diag = index
    for y in range(n):
        I[index] = (y, y)
        index += 1
    end_diag = index - 1
    # indeksy elementow nad przekatna
    for y in range(n-1):
        for x in range(y+1, n):
            print(y, x)
            I[index] = (y, x)
            index += 1
    
    quickselect(T, 0, (n**2)-1, start_diag, I)
    quickselect(T, start_diag+1, (n**2)-1, end_diag, I)

runtests( Median ) 
