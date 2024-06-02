from egz1atesty import runtests

def snow( S ):
    S = sorted(S, reverse=True)
    days_passed = 0
    result = 0
    for s in S:
        if s <= days_passed:
            break
        result += s - days_passed
        days_passed += 1
    
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
