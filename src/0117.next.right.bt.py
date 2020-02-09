"""Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
  def connect(self, root: 'Node') -> 'Node':
    """Two pointer, maintain poiner i, j where i is on one level up of j to create jump connections.
      Move from level k to level k + 1 only when level k is complete, just as level order traversal.
    """
    if root is None:
      return root
    li, lj = root, root.left or root.right
    while li and lj:
      ni, nj = li, lj
      li, lj = lj, None
      while ni is not None:
        if lj is None:
          if nj.left is not None:
            lj = nj.left
          elif nj.right is not None:
            lj = nj.right
        if ni.left is not None and ni.left is not nj:
          nj.next = ni.left
          nj = nj.next
          if lj is None:
            if nj.left is not None:
              lj = nj.left
            elif nj.right is not None:
              lj = nj.right
        if ni.right is not None and ni.right is not nj:
          nj.next = ni.right
          nj = nj.next
          if lj is None:
            if nj.left is not None:
              lj = nj.left
            elif nj.right is not None:
              lj = nj.right
        ni = ni.next
    return root
