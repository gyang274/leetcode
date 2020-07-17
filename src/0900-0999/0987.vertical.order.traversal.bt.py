from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, x, y):
    self.xyz.append((x, y, node.val))
    if node.left:
      self.recursive(node.left, x - 1, y + 1)
    if node.right:
      self.recursive(node.right, x + 1, y + 1)
  def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    self.xyz = []
    self.recursive(root, 0, 0)
    self.xyz.sort()
    xs, ans = float('-inf'), []
    print(self.xyz)
    for x, y, z in self.xyz:
      if x > xs:
        ans.append([z])
        xs = x
      else:
        ans[-1].append(z)
    return ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,2,3,4,5,6,7],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.verticalTraversal(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
