"""
# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children if children is not None else []
"""

class Solution:
  def findRoot(self, tree: List['Node']) -> 'Node':
    # TC: O(N), SC: O(1).
    # node with indegree 0 is the root, e.g., not a child of anyone
    # use xor since each none root node shows up as child once and only once
    v = 0
    for node in tree:
      v ^= node.val
      for child in node.children:
        v ^= child.val
    for node in tree:
      if node.val == v:
        return node
    return None
