from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def backtrack(self, path, node):
    path += str(node.val) + "->"
    if not node.left and not node.right:
      self.ans.append(path[:-2])
    else:
      if node.left:
        self.backtrack(path, node.left)
      if node.right:
        self.backtrack(path, node.right)
  def binaryTreePaths(self, root: TreeNode) -> List[str]:
    """backtrack
    """
    self.ans = []
    if root:
      self.backtrack("", root)
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # [],
    [1],
    [1,2,3,4,5],
    [1,2,3,None,5],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [solver.binaryTreePaths(root) for root in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()} | solution: {rs}")