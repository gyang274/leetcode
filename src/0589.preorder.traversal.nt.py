"""Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children
"""

class Solution:
  def recursive(self, node):
    self.stack.append(node.val)
    for child in node.children:
      self.recursive(child)
  def preorder(self, root: 'Node') -> List[int]:
    self.stack = []
    if root:
      self.recursive(root)
    return self.stack

class Solution:
  def preorder(self, root: 'Node') -> List[int]:
    stack, queue = [], [root]
    if root:
      while queue:
        node = queue.pop()
        stack.append(node.val)
        if node.children:
          queue.extend(node.children[::-1])
    return stack
