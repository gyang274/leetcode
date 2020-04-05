from typing import List
from collections import Counter
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    sl, sr = 0, 0
    if node.left:
      sl = self.recursive(node.left)
    if node.right:
      sr = self.recursive(node.right)
    sn = node.val + sl + sr
    self.ss.append(sn)
    return sn
  def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
    self.ss = []
    if root:
      self.recursive(root)
    cntr = Counter(self.ss)
    cmax = max(list(cntr.values())) if self.ss else 0
    return [k for k in cntr if cntr[k] == cmax]

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [1],
    [1,None,2,3],
    [2,-1,3,-4,5],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.findFrequentTreeSum(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
