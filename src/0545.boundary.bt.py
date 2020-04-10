from typing import List
from config.treenode import TreeNode, listToTreeNode
from collections import deque

class Solution:
  def leftmost(self, node):
    x = []
    while node:
      x.append(node)
      if node.left:
        node = node.left
      elif node.right:
        node = node.right
      else:
        break
    return x
  def rightmost(self, node):
    x = []
    while node:
      x.append(node)
      if node.right:
        node = node.right
      elif node.left:
        node = node.left
      else:
        break
    return x
  def leaves(self, node):
    x = []
    if node:
      stack = deque([node])
      while stack:
        node = stack.pop()
        if not (node.left or node.right):
          x.append(node)
        else:
          if node.right:
            stack.append(node.right)
          if node.left:
            stack.append(node.left)
    return x
  def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
    if not root:
      return []
    xl = self.leftmost(root.left)
    xlv = self.leaves(root.left)
    if xl and xlv and xlv[0] == xl[-1]:
      xl.pop()
    xr = self.rightmost(root.right)
    xrv = self.leaves(root.right)
    if xr and xrv and xrv[-1] == xr[-1]:
      xr.pop()
    return [node.val for node in [root] + xl + xlv + xrv + xr[::-1]]

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [1,None,2,3],
    # [1,None,2,3,4],
    [1,2,7,3,5,None,6,4]
    # [1,2,3,4,5,6,None,None,None,7,8,9,10],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.boundaryOfBinaryTree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
