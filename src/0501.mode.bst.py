from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive1st(self, node):
    # left
    if node.left:
      self.recursive1st(node.left)
    # handle this node
    if self.currVal == node.val:
      self.currCount += 1
    else:
      self.currVal = node.val
      self.currCount = 1
    self.modeCount = max(self.modeCount, self.currCount)
    # right
    if node.right:
      self.recursive1st(node.right)
  def recursive2nd(self, node):
     # left
    if node.left:
      self.recursive2nd(node.left)
    # handle this node
    if self.currVal == node.val:
      self.currCount += 1
    else:
      self.currVal = node.val
      self.currCount = 1
    if self.currCount == self.modeCount:
      self.mode.append(node.val)
    # right
    if node.right:
      self.recursive2nd(node.right)  
  def findMode(self, root: TreeNode) -> List[int]:
    """TC: O(N), SC: O(1), two pass, 1st pass count max occurrence, 2nd pass output.
    """
    self.mode = []
    self.modeCount = 0
    self.currVal = 0
    self.currCount = 0
    if root:
      self.recursive1st(root)
      self.currVal = 0
      self.currCount = 0
      self.recursive2nd(root)
    return self.mode

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1],
    [2147483647],
    [1,None,2,2],
    [1,None,2,3],
    [6,2,8,0,4,7,9,None,None,2,6],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.findMode(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
