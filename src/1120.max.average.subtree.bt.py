from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    if not (node.left or node.right):
      self.xmax = max(self.xmax, node.val)
      return node.val, 1
    xl, nl = 0, 0
    if node.left:
      xl, nl = self.recursive(node.left)
    xr, nr = 0, 0
    if node.right:
      xr, nr = self.recursive(node.right)
    x, n = node.val + xl + xr, 1 + nl + nr
    self.xmax = max(self.xmax, x / n)
    return x, n
  def maximumAverageSubtree(self, root: TreeNode) -> float:
    self.xmax = -1
    self.recursive(root)
    return self.xmax

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,3,2],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.maximumAverageSubtree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
