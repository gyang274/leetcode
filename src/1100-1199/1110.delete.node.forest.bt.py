from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    if node.val in self.ds:
      self.ans.discard(node)
      if node.left:
        self.ans.add(node.left)
      if node.right:
        self.ans.add(node.right)
    if node.left:
      self.recursive(node.left)
      if node.left.val in self.ds:
        node.left = None
    if node.right:
      self.recursive(node.right)
      if node.right.val in self.ds:
        node.right = None
  def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    self.ans, self.ds = {root}, set(to_delete)
    self.recursive(root)
    return self.ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,2,3,4,5,6,7], [3,5]),
  ]
  cases = [
    (listToTreeNode(x), to_delete) for x, to_delete in cases
  ]
  rslts = [
    solver.delNodes(root, to_delete) for root, to_delete in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None} + {cs[1]}\nsolution: {rs}")
