from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node: TreeNode) -> int:
    if not node:
      return -1
    nl = self.recursive(node.left)
    nr = self.recursive(node.right)
    n = max(nl, nr) + 1
    if n > len(self.ans) - 1:
      self.ans.append([node.val])
    else:
      self.ans[n].append(node.val)
    return n
  def findLeaves(self, root: TreeNode) -> List[List[int]]:
    """modified postorder traversal.
    """
    self.ans = []
    if root:
      _ = self.recursive(root)
    return self.ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1],
    [1,2],
    [1,2,None,3],
    [1,2,3,None,4,5],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.findLeaves(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")