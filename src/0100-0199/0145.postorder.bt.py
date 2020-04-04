from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def postorderTraversalRecursive(self, x, root):
    if root.left is not None:
      self.postorderTraversalRecursive(x, root.left)
    if root.right is not None:
      self.postorderTraversalRecursive(x, root.right)
    x.append(root.val)
  def postorderTraversal(self, root: TreeNode) -> List[int]:
    """Recursive.
    """
    x = []
    if root is not None:
      self.postorderTraversalRecursive(x, root)
    return x

class Solution:
  def postorderTraversal(self, root: TreeNode) -> List[int]:
    """Iterative.
    """
    x = []
    if root is not None:
      stack = [root, ]
      while stack:
        node = stack.pop()
        x.append(node.val)
        if node.left is not None:
          stack.append(node.left)
        if node.right is not None:
          stack.append(node.right)
    return list(reversed(x))

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.postorderTraversal(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None}, solution: {rs}")
