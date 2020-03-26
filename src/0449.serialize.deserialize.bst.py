from config.treenode import TreeNode
from collections import deque

class Codec:
  """Q0297, check out listToTreeNode in @/src/config/treenode.py, which is exactly how deserialize work.
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

class Codec:
  """optimize the encoded str size for transmission.
    1. Binary tree could be constructed from preorder/postorder and inorder traversal.
    2. Inorder traversal of BST is an array sorted in the ascending order: inorder = sorted(preorder).
  """
  def serialize(self, root: TreeNode) -> str:
    """Encodes a tree to a single string.
    """
    x = []
    if root:
      stack = [root, ]
      while stack:
        node = stack.pop()
        x.append(node.val)
        if node.right:
          stack.append(node.right)
        if node.left:
          stack.append(node.left)
    return ' '.join(map(str, x))

  def deserialize(self, data: str) -> TreeNode:
    """Decodes your encoded data to tree.
    """
    x = deque([int(v) for v in data.split()])
    if not x:
      return None
    root = TreeNode(x.popleft())
    # decode w.r.t bst property
    stack = [root]
    while x:
      node = TreeNode(x.popleft())
      if node.val < stack[-1].val:
        stack[-1].left = node
      else:
        while stack and node.val > stack[-1].val:
          hold = stack.pop()
        hold.right = node  
      stack.append(node)
    return root
