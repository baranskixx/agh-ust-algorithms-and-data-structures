from zad2testy import runtests

def tower(A):
    stack = []
    result = 0
    for a, b in A:
        while stack and (stack[-1][0] > a or stack[-1][1] < b):
            stack.pop()
        stack.append((a, b))
        result = max(result, len(stack))
    return result

runtests(tower)
