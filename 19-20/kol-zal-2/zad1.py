from zad1testy import runtests

"""
Autor rozwiązania: Adam Barański
Zlozonosc: O(n * log(n))

Sortujemy punkty najpierw po y, potem po x rosnaco (sortowanie stabilne)
Nastepnie przechodzimy po kolejnych punktach, zapisujac ostatni dominujacy punkt
Jesli znajdziemy, punkt ktorego dominujacy punkt nie dominuje to go nadpisujemy tym znalezionym
"""

def dominance(P):
    n = len(P)
    P = [(P[i][0], P[i][1], i) for i in range(n)]
    P = sorted(P, key=lambda x : x[1])
    P = sorted(P, key=lambda x : x[0])

    S = [P[0][2]]
    curr_x, curr_y, _ = P[0]
 
    for point in P:
        x, y, org_index = point
        if curr_x > x or curr_y > y:
            curr_x, curr_y = x, y
            S.append(org_index)
    
    return S

runtests( dominance ) 
