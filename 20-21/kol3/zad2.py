from zad2testy import runtests

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

INF = 1e9

def cutthetree(T):
    def rek(node):
        if node.left is None and node.right is None:
            return INF
        elif node.left is None:
            return min(node.value, rek(node.right))
        elif node.right is None:
            return min(node.value, rek(node.left))
        return min(node.value, rek(node.left) + rek(node.right))
    return rek(T.left) + rek(T.right)

    
runtests(cutthetree)


