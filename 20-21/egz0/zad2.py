from zad2testy import runtests


class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval = 0  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane


def valuableTree(T, k):
    def dfs(node):
        if node is None:
            return [0] * (k + 1)

        left = dfs(node.left)
        right = dfs(node.right)

        node.X = [0] * (k + 1)

        for i in range(k + 1):
            for j in range(i + 1):
                if i - j - 1 >= 0:
                    node.X[i] = max(node.X[i], left[j] + right[i - j - 1] + node.leftval + node.rightval)
                if j >= 0:
                    node.X[i] = max(node.X[i], left[j] + right[i - j] + node.rightval)
                if i - j >= 0:
                    node.X[i] = max(node.X[i], left[j] + right[i - j] + node.leftval)

        return node.X

    result = dfs(T)
    return max(result)


runtests(valuableTree)
