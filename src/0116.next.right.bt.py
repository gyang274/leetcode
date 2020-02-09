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
    li = root
    while li and li.left:
      ni, nj = li, li.left
      while ni.next:
        nj.next = ni.right
        ni = ni.next
        nj = nj.next
        nj.next = ni.left
        nj = nj.next
      nj.next = ni.right
      li = li.left
    return root


class Solution:
  def connect(self, root: 'Node') -> 'Node':
    """Two pointer, maintain poiner i, j where i is on one level up of j to create jump connections.
      Move from level k to level k + 1 only when level k is complete, just as level order traversal.
    """
    if root is None:
      return root
    li = root
    while li and li.left:
      ni, nj = li, li.left
      nj.next = ni.right
      while ni.next:
        ni = ni.next
        nj = nj.next
        nj.next = ni.left
        nj = nj.next
        nj.next = ni.right
      li = li.left
    return root