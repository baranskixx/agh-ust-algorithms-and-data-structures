from egz1atesty import runtests

"""
Autor rozwiazania: Adam Baranski

Złozonosc obliczeniowa: O(n)
Nie wiem czemu to dziala tak

"""


def snow( S ):
    S = sorted(S, reverse=True)
    result = 0
    for i, s in enumerate(S):
        if s <= i:
            break
        result += s - i

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
