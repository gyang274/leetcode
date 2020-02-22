from typing import List
from config.treenode import TreeNode, listToTreeNode


class Solution:
  def recursive(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    v = postorder[-1]
    i = inorder.index(v)
    root = TreeNode(v)
    if i > 0:
      root.left = self.recursive(inorder[:i], postorder[:i])
    if i < len(inorder) - 1:
      root.right = self.recursive(inorder[(i + 1):], postorder[i:(len(postorder)-1)])
    return root
  def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if not (inorder and postorder):
      return None
    return self.recursive(inorder, postorder)


class Solution:
  def recursive(self, l, r) -> TreeNode:
    """Args:
      l, r: sub-inorder formed from self.inorder[l:r], l < r
    """
    v = self.postorder[self.postindex]
    i = self.inorder[v]
    self.postindex -= 1
    root = TreeNode(v)
    if i < r - 1:
      root.right = self.recursive(i + 1, r)
    if i > l:
      root.left = self.recursive(l, i)
    return root
  def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    """use pointer to avoid copy of lists
    """
    if not (inorder and postorder):
      return None
    self.inorder = {}
    for i, v in enumerate(inorder):
      self.inorder[v] = i
    self.postorder = postorder
    self.postindex = -1
    return self.recursive(0, len(inorder))


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([3,2,1], [3,2,1]),
    ([9,3,15,20,7], [9,15,7,20,3]),
  ]
  rslts = [
    solver.buildTree(preorder, inorder) for preorder, inorder in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs}, solution:\n{rs.display()}")