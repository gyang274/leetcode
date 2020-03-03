# Definition for a binary tree node.
# class TreeNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.left = None
#     self.right = None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

from config.treenode import TreeNode
from collections import deque

class Codec:
  """check out listToTreeNode in @/src/config/treenode.py, which is exactly how deserialize work.
  """
  def serialize(self, root: TreeNode) -> str:
    """Encodes a tree to a single string.
    """
    # use empty space to represent None in str, still use comma as separator
    s, stack = "", deque([root, ])
    if root:
      while stack:
        node = stack.popleft()
        if node:
          s += str(node.val) + ","
          stack.append(node.left)
          stack.append(node.right)
        else:
          s += " ,"
    return s[:-1]
  def deserialize(self, data: str) -> TreeNode:
    """Decodes your encoded data to tree.
    """
    x = deque(data.split(','))
    v = x.popleft()
    if v == "" or v == " ":
      return None
    root = TreeNode(v)
    stack = deque([root, ])
    while x:
      node = stack.popleft()
      v = x.popleft()
      if not v == " ":
        node.left = TreeNode(v)
        stack.append(node.left)
      if x:
        v = x.popleft()
        if not v == " ":
          node.right = TreeNode(v)
          stack.append(node.right)
    return root
