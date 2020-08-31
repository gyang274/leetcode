from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, level):
    if level > len(self.s):
      self.s.append(0)
    self.s[level - 1] += node.val
    if node.left:
      self.recursive(node.left, level + 1)
    if node.right:
      self.recursive(node.right, level + 1)
  def maxLevelSum(self, root: TreeNode) -> int:
    # self.s: self.s[i] is i-th level sum
    self.s = []
    self.recursive(root, 1)
    ms = max(self.s)
    for i in range(len(self.s)):
      if self.s[i] == ms:
        return i + 1
    return 0

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
    [1,7,0,7,-8,None,None],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.maxLevelSum(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
