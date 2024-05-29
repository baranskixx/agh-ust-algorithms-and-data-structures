from zad2testy import runtests


def opt_sum(tab):
    n = len(tab)
    
    # dp[i][j] będzie przechowywać minimalną maksymalną wartość bezwzględną wyniku tymczasowego
    dp = [[float('inf')] * n for _ in range(n)]
    
    # S[i][j] będzie przechowywać sumę liczb tab[i:j+1]
    S = [[0] * n for _ in range(n)]
    
    # Inicjalizacja tablicy S
    for i in range(n):
        S[i][i] = tab[i]
        for j in range(i+1, n):
            S[i][j] = S[i][j-1] + tab[j]
    
    # Inicjalizacja tablicy dp dla podtablic o długości 1
    for i in range(n):
        dp[i][i] = abs(tab[i])
    
    # Obliczenie dp dla podtablic o długości większej niż 1
    for length in range(2, n+1):  # length to długość podtablicy
        for i in range(n-length+1):
            j = i + length - 1
            for k in range(i, j):
                temp_max = max(dp[i][k], dp[k+1][j], abs(S[i][j]))
                dp[i][j] = min(dp[i][j], temp_max)
    
    return dp[0][n-1]



runtests( opt_sum )
