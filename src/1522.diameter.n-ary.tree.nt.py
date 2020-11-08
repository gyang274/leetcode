"""
# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children if children is not None else []
"""

import heapq

class Solution:
  def recursive(self, node):
    ms = [self.recursive(child) for child in node.children]
    if ms:
      self.d = max(self.d, sum(heapq.nlargest(2, ms)))
    return (max(ms) if ms else 0) + 1
  def diameter(self, root: 'Node') -> int:
    self.d = 0
    self.recursive(root)
    return self.d
