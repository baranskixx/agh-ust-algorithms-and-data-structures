from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def find_max_depth(node, depth = 0):
  if node is None:
    return 0
  if node.left is None and node.right is None:
    return depth
  return max(find_max_depth(node.left, depth+1), find_max_depth(node.right, depth+1))

def count_nodes_on_each_level(root):
  n = find_max_depth(root)
  NODES = [0] * (n+1)

  def rek(node, depth=0):
    if node is None:
      return
    NODES[depth] += 1
    rek(node.left, depth+1)
    rek(node.right, depth+1)
  
  rek(root)
  return NODES

def find_max_depth_for_each_subtree(root):
  def rek(node, depth = 0):
    if node is None:
      return 0
    node.x = max(depth, rek(node.left, depth+1), rek(node.right, depth+1))
    return node.x
  rek(root)
  return root

def count_removed_edges(root, max_width_level):
  edges_removed = 0
  def rek(node, level = 0):
    nonlocal edges_removed
    if level == max_width_level:
      if node.left is not None:
        edges_removed += 1
      if node.right is not None:
        edges_removed += 1
    else:
      if node.left is not None:
        if node.left.x < max_width_level:
          edges_removed += 1
        else:
          rek(node.left, level+1)
      if node.right is not None:
        if node.right.x < max_width_level:
          edges_removed += 1
        else:
          rek(node.right, level+1)
  rek(root)
  return edges_removed
    
    
def wideentall( T ):
  CNT = count_nodes_on_each_level(T)
  T = find_max_depth_for_each_subtree(T)
  max_width = -1
  max_width_level = -1
  print(CNT)
  for i, t in enumerate(CNT):
    if t >= max_width:
      max_width = t
      max_width_level = i
  
  return count_removed_edges(T, max_width_level)
  
    
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )