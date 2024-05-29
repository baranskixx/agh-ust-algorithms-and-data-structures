from zad1testy import Node, runtests
from collections import deque


def inorder_traversal(root):
    nodes = []

    def traverse(node):
        if node is not None:
            traverse(node.left)
            nodes.append(node)
            traverse(node.right)

    traverse(root)
    return nodes

def build_min_height_tree(nodes):
    n = len(nodes)
    Q = deque([0])
    x = 1

    while len(Q) != 0:
        u = Q.popleft()

        parent_node = nodes[u]
        left = None
        right = None
        if x < n:
            left = nodes[x]
            left.parent = parent_node
            Q.append(x)
        if x + 1 < n:
            right = nodes[x+1] 
            right.parent = parent_node
            Q.append(x+1)
        x += 2

        parent_node.left = left
        parent_node.right = right 
    
    return nodes[0]
        
    

def convert_tree(T):
    nodes = inorder_traversal(T)
    return build_min_height_tree(nodes)

runtests(convert_tree)