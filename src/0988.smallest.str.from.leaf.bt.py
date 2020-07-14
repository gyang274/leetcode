from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, path, node):
    x = chr(node.val + 97)
    if node.left or node.right:
      if node.left:
        self.recursive(x + path, node.left)
      if node.right:
        self.recursive(x + path, node.right)
    else:
      if x < self.s[0]:
        self.s = x + path
      elif x == self.s[0]:
        self.s = min(x + path, self.s)
  def smallestFromLeaf(self, root: TreeNode) -> str:
    self.s = '\x7f'
    self.recursive('', root)
    return self.s

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
    [0,1,2,3,4,3,4],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.smallestFromLeaf(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
