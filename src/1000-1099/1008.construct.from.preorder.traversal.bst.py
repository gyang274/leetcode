from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    n = len(preorder)
    if not n:
      return None
    root = TreeNode(preorder[0])
    stack = [root]
    for i in range(1, n):
      node, child = stack[-1], TreeNode(preorder[i])
      while stack and stack[-1].val < child.val:
        node = stack.pop()
      if node.val > child.val:
        node.left = child
      else:
        node.right = child
      stack.append(child)
    return root

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [8,5,1,7,10,12],
  ]
  rslts = [solver.bstFromPreorder(preorder) for preorder in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution:\n{rs.display() if rs else None}")
