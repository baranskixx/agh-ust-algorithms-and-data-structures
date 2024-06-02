from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def find_height(p, height = 0):
  if p is None:
    return height 
  return max(
    find_height(p.left, height+1), 
    find_height(p.right, height+1)
  )
  
def wideentall( T ):
  height = find_height(T)
  W = [0 for _ in range(height)]
  def traverse(p, level):
    if p is not None:
      W[level] += 1
      traverse(p.left, level+1)
      traverse(p.right, level+1)
  traverse(T, 0)

  max_width = -1
  min_cost = 1e9

  for i, cnt in enumerate(W):
    if cnt > max_width:
      max_width = cnt
      min_cost = W[i+1] if i+1 < height else 0
    if cnt == max_width:
      min_cost = min(min_cost, W[i+1] if i+1 < height else 0)
  
  return min_cost

    
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )