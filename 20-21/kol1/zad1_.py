from zad1testy import runtests


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
    T2 = [0] * (n * n)

    for y in range(n):
        for x in range(n):
            T2[y * n + x] = T[y][x]

    d1 = (n**2 - n) //  2
    d2 = (n**2 + n) //  2


    print(d1, d2)

runtests( Median ) 