"""Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children
"""
"""Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
"""

from collections import deque

class Codec:
  
  def encode(self, root: 'Node') -> TreeNode:
    # Encodes an n-ary tree to a binary tree.
    # use TreeNode left as Node to 1st child, and TreeNode right as links to siblings.
    if not root:
      return None
    stack = deque([root, ])
    while stack:
      node = stack.popleft()
      if not hasattr(node, 'left'):
        node.left = None
      if not hasattr(node, 'right'):
        node.right = None
      if node.children:
        node.left = node.children[0]
        for i in range(len(node.children) - 1):
          node.children[i].right = node.children[i + 1]
          stack.append(node.children[i])
        stack.append(node.children[-1])
      # node.children = None
      delattr(node, 'children')
    return root
 
  def decode(self, data: TreeNode) -> 'Node':
    # Decodes your binary tree to an n-ary tree.
    if not data:
      return None
    stack = deque([data, ])
    while stack:
      node = stack.popleft()
      node.children = []
      if node.left:
        nc = node.left
        node.children.append(nc)
        while nc.right:
          nc = nc.right
          node.children.append(nc)
      delattr(node, 'left')
      delattr(node, 'right') 
      stack.extend(node.children)
    return data