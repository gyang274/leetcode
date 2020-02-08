from typing import List
from config.treenode import TreeNode, listToTreeNode


class Solution:
  def recursive(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    v = preorder[0]
    i = inorder.index(v)
    root = TreeNode(v)
    if i > 0:
      root.left = self.recursive(preorder[1:(1 + i)], inorder[:i])
    if i < len(inorder) - 1:
      root.right = self.recursive(preorder[(i + 1):], inorder[(i + 1):])
    return root
  def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if not (preorder and inorder):
      return None
    return self.recursive(preorder, inorder)


class Solution:
  def recursive(self, l, r) -> TreeNode:
    """Args:
      l, r: sub-inorder formed from self.inorder[l:r], l < r
    """
    v = self.preorder[self.preindex]
    i = self.inorder[v]
    self.preindex += 1
    root = TreeNode(v)
    if i > l:
      root.left = self.recursive(l, i)
    if i < r - 1:
      root.right = self.recursive(i + 1, r)
    return root
  def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    """use pointer to avoid copy of lists
    """
    if not (preorder and inorder):
      return None
    self.preorder = preorder
    self.inorder = {}
    for i, v in enumerate(inorder):
      self.inorder[v] = i
    self.preindex = 0
    return self.recursive(0, len(inorder))


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,2,3], [3,2,1]),
    ([3,9,20,15,7], [9,3,15,20,7]),
  ]
  rslts = [
    solver.buildTree(preorder, inorder) for preorder, inorder in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs}, solution:\n{rs.display()}")