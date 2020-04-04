from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def preorderTraversalRecursive(self, x, root):
    x.append(root.val)
    if root.left is not None:
      self.preorderTraversalRecursive(x, root.left)
    if root.right is not None:
      self.preorderTraversalRecursive(x, root.right)
  def preorderTraversal(self, root: TreeNode) -> List[int]:
    """Recursive.
    """
    x = []
    if root is not None:
      self.preorderTraversalRecursive(x, root)
    return x

class Solution:
  def preorderTraversal(self, root: TreeNode) -> List[int]:
    """Iterative.
    """
    x = []
    if root is not None:
      stack = [root, ]
      while stack:
        node = stack.pop()
        x.append(node.val)
        if node.right is not None:
          stack.append(node.right)
        if node.left is not None:
          stack.append(node.left)
    return x

class Solution:
  def preorderTraversal(self, root: TreeNode) -> List[int]:
    """Morris Traversal.
    """
    node, x = root, []
    while node is not None:
      if node.left is None:
        x.append(node.val)
        node = node.right
      else:
        prev = node.left
        while prev.right is not None and prev.right is not node:
          prev = prev.right
        if prev.right is None:
          x.append(node.val)
          prev.right = node
          node = node.left
        else:
          prev.right = None
          node = node.right
    return x

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.preorderTraversal(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None}, solution: {rs}")
