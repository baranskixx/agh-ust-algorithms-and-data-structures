from egz2btesty import runtests


def magic(C):
    INF = 1e9
    n = len(C)
    print(n)
    F = [-1] * n
    F[0] = 0
    
    for i in range(n):
        in_chest = C[i][0]
        current_gold = F[i]
        if current_gold == -1:
            continue

        for gold_to_open, u in C[i][1:]:
            if u == -1:
                continue
            else:
                diff = gold_to_open - in_chest
                if (diff < 0 and diff >= -10) or (diff >= 0 and current_gold - diff >= 0):
                    F[u] = max(F[u], current_gold - diff)
    return F[-1]
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )