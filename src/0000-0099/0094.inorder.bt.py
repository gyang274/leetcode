from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def inorderTraversalRecursive(self, x, root):
    if root.left is not None:
      self.inorderTraversalRecursive(x, root.left)
    x.append(root.val)
    if root.right is not None:
      self.inorderTraversalRecursive(x, root.right)
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    """Recursive.
    """
    x = []
    if root is not None:
      self.inorderTraversalRecursive(x, root)
    return x

class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    """Iterative.
    """
    x = []
    if root is not None:
      node, stack = root, []
      while node or stack:
        while node is not None:
          stack.append(node)
          node = node.left
        node = stack.pop()
        x.append(node.val)
        node = node.right
    return x

class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    """Morris Traversal.
    """
    x = []
    if root is not None:
      node = root
      while node:
        if not node.left:
          x.append(node.val)
          node = node.right
        else:
          prev = node.left
          while prev.right:
            prev = prev.right
          prev.right = node
          # hold = node
          # node = node.left
          # hold.left = None
          # note: node, node.left =  node.left , None; will cause loop, wrong!
          node.left, node = None, node.left 
    return x

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1, None, 2, 3]
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.inorderTraversal(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")