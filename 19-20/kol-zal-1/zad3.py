from zad3testy import runtests

"""
Autor rozwiązania: Adam Barański
Zlozonosc: O(n * logk)
Korzystamy z drzewa BST i sliding window do znajdywania maksymalnego
podciagu bez wszystkich elementow
"""


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.count = 1  # Licznik wystąpień tego klucza w drzewie

class BST:
    def __init__(self):
        self.root = None
        self.unique_count = 0  # Licznik unikalnych elementów w drzewie
    
    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
            self.unique_count += 1
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
                self.unique_count += 1
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key)
                self.unique_count += 1
            else:
                self._insert(node.right, key)
        else:  # key == node.key
            node.count += 1
    
    def remove(self, key):
        self.root, removed = self._remove(self.root, key)
        if removed:
            self.unique_count -= 1
    
    def _remove(self, node, key):
        if node is None:
            return node, False
        
        if key < node.key:
            node.left, removed = self._remove(node.left, key)
        elif key > node.key:
            node.right, removed = self._remove(node.right, key)
        else:  # key == node.key
            if node.count > 1:
                node.count -= 1
                return node, False
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            
            min_larger_node = self._find_min(node.right)
            node.key, node.count = min_larger_node.key, min_larger_node.count
            min_larger_node.count = 1
            node.right, _ = self._remove(node.right, min_larger_node.key)
            return node, False
        
        return node, removed
    
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def contains(self, key):
        return self._contains(self.root, key)
    
    def _contains(self, node, key):
        if node is None:
            return False
        if key < node.key:
            return self._contains(node.left, key)
        elif key > node.key:
            return self._contains(node.right, key)
        else:  # key == node.key
            return True


def longest_incomplete(A, k):
    n = len(A)
    bst = BST()
    left = 0
    max_length = 0
    
    for right in range(n):
        bst.insert(A[right])
        
        while bst.unique_count == k:
            bst.remove(A[left])
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length



runtests( longest_incomplete ) 
