from config.treenode import TreeNode, listToTreeNode
from collections import defaultdict

class Solution:
  def recursive(self, node, i):
    self.d[i].append(node.val)
    if node.left:
      self.recursive(node.left, i + 1)
    if node.right:
      self.recursive(node.right, i + 1)
  def isEvenOddTree(self, root: TreeNode) -> bool:
    self.d = d = defaultdict(list)
    self.recursive(root, 0)
    for k in d:
      if k & 1:
        if any(x & 1 for x in d[k]) or any(x <= y for x, y in zip(d[k][:-1], d[k][1:])):
          return False
      else:
        if any((x & 1) ^ 1 for x in d[k]) or any(x >= y for x, y in zip(d[k][:-1], d[k][1:])):
          return False
    return True

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1],
    [1,None,2,3],
    [5,4,2,3,3,7],
    [5,9,1,3,5,7],
    [2,12,8,5,9,None,None,18,16],
    [1,10,4,3,None,7,9,12,8,6,None,None,2],
    [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.isEvenOddTree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
