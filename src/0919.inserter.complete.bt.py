from config.treenode import TreeNode, listToTreeNode
from collections import deque

class CBTInserter:

  def __init__(self, root: TreeNode):
    self.root = root
    # nodes subject to insert
    self.q = deque([])
    # level order traversal
    queue = deque([root])
    while queue:
      node = queue.popleft()
      if node.right:
        queue.append(node.left)
        queue.append(node.right)
      elif node.left:
        queue.append(node.left)
        self.q.append([1, node])
      else:
        self.q.append([0, node])

  def insert(self, v: int) -> int:
    # create and connect
    node = TreeNode(v)
    if self.q[0][0]:
      self.q[0][1].right = node
    else:
      self.q[0][1].left = node
    x = self.q[0][1].val
    # pop if complete
    self.q[0][0] += 1
    if self.q[0][0] == 2:
      self.q.popleft()
    # append new node
    self.q.append([0, node])
    return x

  def get_root(self) -> TreeNode:
    return self.root