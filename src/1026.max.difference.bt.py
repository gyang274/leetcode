from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, xmin, xmax):
    xmin = min(xmin, node.val)
    xmax = max(xmax, node.val)
    self.dmax = max(self.dmax, xmax - xmin)
    if node.left:
      self.recursive(node.left, xmin, xmax)
    if node.right:
      self.recursive(node.right, xmin, xmax)
  def maxAncestorDiff(self, root: TreeNode) -> int:
    self.dmax = 0
    self.recursive(root, root.val, root.val)
    return self.dmax

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
    [8,3,10,1,6,None,14,None,None,4,7,11],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.maxAncestorDiff(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
