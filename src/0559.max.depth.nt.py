"""Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children
"""

class Solution:
  def maxDepth(self, root: 'Node') -> int:
    d = 0
    if root:
      d += 1
      if root.children:
        d += max([self.maxDepth(x) for x in root.children])
    return d