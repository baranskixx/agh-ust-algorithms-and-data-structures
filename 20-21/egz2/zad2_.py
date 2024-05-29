from zad2testy import runtests
from collections import deque

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


def calculate_tree_sum(p):
    for i in range(len(p.edges)):
        p.tree_sum += p.weights[i]
        p.tree_sum += calculate_tree_sum(p.edges[i])
    
    return p.tree_sum

def find_min_edge(root):
    min_edge_id = -1
    min_diff = 1e9
    Q = deque()
    Q.append(root)

    while len(Q) != 0:
        p = Q.popleft()

        for i in range(len(p.weights)):
            Q.append(p.edges[i])
            diff = abs(root.tree_sum - p.weights[i] - 2 * (p.edges[i].tree_sum))
            if diff <= min_diff:
                min_diff = diff
                min_edge_id = p.ids[i]
    
    return min_edge_id


def balance( T ):
    calculate_tree_sum(T)
    return find_min_edge(T)
    

runtests( balance )
