"""Definition for a Node.
class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random
"""
from collections import defaultdict

class Solution:
  def copyRandomList(self, head: 'Node') -> 'Node':
    """create copy follow the next pointer, keep a reference of each node random_index.
    """
    # s: start
    s = Node(0)
    s.next = head
    # ridx: random_index
    # keyed by random_index node being pointed, values are the node pointing to node with this random_index
    hold, x, ridx = s, head, defaultdict(list)
    while x:
      # create a copy of node
      node = Node(x.val)
      # complete prev's next pointer
      hold.next = node
      # add x.random into ridx
      if x.random is not None:
        ridx[x.random].append(node)
      hold, x = node, x.next
    # complete all y such that y.random -> x (node)
    node, x = s.next, head
    while x:
      if x in ridx:
        yset = ridx.pop(x)
        for y in yset:
          y.random = node
      x, node = x.next, node.next
    return s.next
