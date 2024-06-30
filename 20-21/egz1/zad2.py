from zad2testy import runtests
from queue import PriorityQueue

"""
Autor rozwiązania: Adam Barański
Idea:
F[y][x][dir][sp] - minimalny czas potrzebny do doprowadzenia robota 
do stanu gotowosci do wyjazdu z pola (y, x), w kierunku o indeksie 'dir' i predokscia o indeksie 'sp'
Co jest tozsame ze znalezieniem rozwiazania (wyciagamy minimum z tablic w polu B)
"""

DIR = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

SPEED = [
    60,
    40,
    30
]
INF = 1e9
TURN_SPEED = 45

def robot(L, A, B):
    height = len(L)
    width  = len(L[0])
    Q = PriorityQueue()
    F = [[[[INF] * len(SPEED) for _ in range(len(DIR))] for _ in range(width)] for _ in range(height)]

    # (odleglosc, y, x, kierunek, szybkosc)
    Q.put((0, A[1], A[0], 0, 0))

    while not Q.empty():
        d, y, x, dir, sp = Q.get()

        if F[y][x][dir][sp] <= d or L[y][x] == 'X':
            continue
        F[y][x][dir][sp] = d
        
        # ruch w tym samym kierunku
        move_y, move_x = DIR[dir]
        Q.put((d + SPEED[sp], y + move_y, x + move_x, dir, min(len(SPEED)-1, sp+1)))
        # obrot w prawo
        Q.put((d + TURN_SPEED, y, x, (dir + 1) % 4, 0))
        # obrot w lewo
        Q.put((d + TURN_SPEED, y, x, (dir - 1) % 4, 0))

    min_res = INF
    dest_x, dest_y = B
    for dir in range(len(DIR)):
        for sp in range(len(SPEED)):
            min_res = min(min_res, F[dest_y][dest_x][dir][sp])
    
    return min_res if min_res != INF else None
    
runtests( robot )


