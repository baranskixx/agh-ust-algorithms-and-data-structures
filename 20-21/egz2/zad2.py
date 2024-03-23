from zad2testy import runtests
from collections import deque

"""
Autor rozwiazania: Adam Baranski
Zlozonosc obliczeniowa: O(n) 
Zlozonosc pamieciowa: O(n)

W kazdym wierzcholku zapisujemy tree_sum (dodatkowe pole) - sume krawedzi drzewa, 
ktorego korzeniem jest dany wierzcholek

Nastepnie przechodzimy w czasie liniowym po wszystkich krawedziach i sprawdzamy z uzyciem
dodanego przez nas pola roznice obu drzew powstalych po usunieciu danej krawedzi.
"""

class Node:
    def __init__( self ):     # stwórz węzeł drzewa
        self.edges   = []     # lista węzłów do których są krawędzie
        self.weights = []     # lista wag krawędzi
        self.ids     = []     # lista identyfikatorów krawędzi
        self.tree_sum = 0
      
    def addEdge( self, x, w, id ):     # dodaj krawędź z tego węzła do węzła x
        self.edges.append( x )       # o wadze w i identyfikatorze id
        self.weights.append( w ) 
        self.ids.append( id )
    
    def __str__( self ):
        s = "["
        for i in range(len(self.edges)):
            s += "[%d,%d,%s]" % (self.ids[i], self.weights[i], str(self.edges[i]))
            s += ","
        s+= "]"
        return s

def calculate_tree_sum(x : Node):
    for i in range(len(x.edges)):
        x.tree_sum += x.weights[i]
        x.tree_sum += calculate_tree_sum(x.edges[i])
    return x.tree_sum

def find_min(root : Node):
    min_diff = 1e12
    min_diff_edge = -1
    tree_sum = root.tree_sum
    Q = deque()
    Q.append(root)
    
    while len(Q) != 0:
        u = Q.popleft()
        for i in range(len(u.edges)):
            Q.append(u.edges[i])
            diff = abs(tree_sum - 2 * u.edges[i].tree_sum - u.weights[i])
            if diff < min_diff:
                min_diff = diff
                min_diff_edge = u.ids[i]
                
    return min_diff_edge

def balance( T ):
    calculate_tree_sum(T)
    return find_min(T)

runtests( balance )


