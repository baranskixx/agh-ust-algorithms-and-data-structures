from egz3btesty import runtests

def uncool( P ):
    n = len(P)
    P = [(P[i][0], P[i][1], i) for i in range(n)]

    P = sorted(P, key = lambda x : x[1])
    P = sorted(P, key = lambda x : x[0])

    x = 0
    for y in range(n):
        while x < y and P[x][1] <P[y][0]:
            x += 1
        if P[x][0] < P[y][0] and P[x][1] < P[y][1]:
            return P[x][2], P[y][2]

         


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )


