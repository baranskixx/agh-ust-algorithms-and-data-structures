from zad2testy import runtests

def fast_list_prepend(L,a):
    new_node = FastListNode(a)

    if L is not None:
        i = 0
        while True:
            new_node.next.append(L)
            if i >= len(L.next):
                break
            L = L.next[i]   
            i += 1
        
    return new_node


class FastListNode:
    def __init__(self, a):
        self.a = a     # przechowywana liczba calkowita
        self.next = [] # lista odnosnikow do innych elementow; poczatkowo pusta

    def __str__(self): # zwraca zawartosc wezla w postaci napisu
        res = 'a: ' + str(self.a) + '\t' + 'next keys: '
        res += str([n.a for n in self.next])
        return res


runtests( fast_list_prepend ) 
