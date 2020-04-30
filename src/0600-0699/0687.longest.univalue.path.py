from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    xl = 1
    if node.left:
      ll, lr = self.recursive(node.left)
      if node.val == node.left.val:
        xl += max(ll, lr)
    xr = 1
    if node.right:
      rl, rr = self.recursive(node.right)
      if node.val == node.right.val:
        xr += max(rl, rr)
    self.xmax = max(self.xmax, xl + xr - 2)
    return xl, xr
  def longestUnivaluePath(self, root: TreeNode) -> int:
    self.xmax = 0
    if root:
      self.recursive(root)
    return self.xmax

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
    [5,4,5,1,1,5],
    [5,4,5,1,1,None,5],
    [1,4,5,4,4,None,5],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.longestUnivaluePath(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
