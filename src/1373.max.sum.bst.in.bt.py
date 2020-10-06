from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    # sbst: subtree isBST,
    # smin: subtree min value,
    # smax: subtree max value,
    # ssum: subtree sum values,
    sbst, smin, smax, ssum = True, node.val, node.val, node.val
    if node.left:
      lbst, lmin, lmax, lsum = self.recursive(node.left)
      sbst = sbst and lbst and lmax < node.val
      smin = min(smin, lmin)
      smax = max(smax, lmax)
      ssum += lsum
    if node.right:
      rbst, rmin, rmax, rsum = self.recursive(node.right)
      sbst = sbst and rbst and rmin > node.val
      smin = min(smin, rmin)
      smax = max(smax, rmax)
      ssum += rsum
    if sbst:
      self.ssum = max(self.ssum, ssum)
    return sbst, smin, smax, ssum
  def maxSumBST(self, root: TreeNode) -> int:
    self.ssum = 0
    self.recursive(root)
    return self.ssum

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [2,1,3],
    [1,None,2,3],
    [1,4,3,2,4,2,5,None,None,None,None,None,None,4,6],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.maxSumBST(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
