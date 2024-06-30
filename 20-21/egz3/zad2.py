from zad2testy import runtests

"""
Autor rozwiazania: Adam Baranski
Zlozonosc obliczeniowa: O(D)

Budujemy drzewo BST skorelowane z napisami 
Zliczamy, ile razy wkladajac do drzewa wyrazy wchodzilismy do danego node'a
"""

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.count = 0
        self.indexes = []
    
    def increase_count(self):
        self.count += 1
    
    
def traverse_word(node, word, index = 0):
    node.increase_count()
    if index == len(word):
        return
    if word[index] == '0':
        node.left = node.left if node.left is not None else Node()
        traverse_word(node.left, word, index+1)
    else:
        node.right = node.right if node.right is not None else Node()
        traverse_word(node.right, word, index+1)

def traverse_find_very_nice_words(root):
    result = []
    
    def rek(node, word = ''):
        if node is None or node.count < 2:
            return
        if node.count >= 2:
            if (node.left is None or node.left.count < 2) and \
                (node.right is None or node.right.count < 2):
                    result.append(word)
                    return
        rek(node.left, word + '0')
        rek(node.right, word + '1')
    
    rek(root)
    return sorted(result)
            
def double_prefix( L ):
    root = Node()

    for word in L:
        traverse_word(root, word)
    
    return traverse_find_very_nice_words(root)


runtests( double_prefix )

