from typing import List
from collections import deque
from config.treenode import TreeNode, listToTreeNode


class Solution:
  def inorderTraversalRecursive(self, x, root):
    if root.left:
      self.inorderTraversalRecursive(x, root.left)
    x.append(root.val)
    if root.right:
      self.inorderTraversalRecursive(x, root.right)
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    """Recursive.
    """
    x = []
    if root:
      self.inorderTraversalRecursive(x, root)
    return x


class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    """Iterative.
    """
    x = []
    if root:
      r = root
      q = deque()
      while r or q:
        while r:
          q.append(r)
          r = r.left
        r = q.pop()
        x.append(r.val)
        r = r.right
    return x


# class Solution:
#   def inorderTraversal(self, root: TreeNode) -> List[int]:
#     """Morris Traversal.
#     """
#     x = []
#     if root:
#       r = root
#       while r:
#         if not r.left:
#           x.append(r.val)
#           r = r.right
#         else:
#           s = r.left
#           while s.right:
#             s = s.right
#           s.right = r
#           # z = r
#           # r = r.left
#           # z.left = None
#           # note: r, r.left =  r.left , None; will cause loop, wrong!
#           r.left, r = None, r.left 
#     return x


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1, None, 2, 3]
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.inorderTraversal(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")

