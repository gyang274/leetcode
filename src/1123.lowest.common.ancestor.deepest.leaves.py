from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, depth):
    # dmax: max-depth of subtree rooted by node
    # dnum: num of nodes with max-depth within subtree rooted by node
    if not (node.left or node.right):
      dmax, dnum = depth, 1
    else:
      dmaxL, dnumL = 0, 0
      if node.left:
        dmaxL, dnumL = self.recursive(node.left, depth + 1)
      dmaxR, dnumR = 0, 0
      if node.right:
        dmaxR, dnumR = self.recursive(node.right, depth + 1)
      dmax = max(dmaxL, dmaxR)
      if dmaxL == dmaxR:
        dnum = dnumL + dnumR
      else:
        dnum = dnumL if dmaxL > dmaxR else dnumR
    # is node LCA of deepest leaves?
    if dmax > self.dmax or (dmax == self.dmax and dnum > self.dnum):
      self.ans, self.dmax, self.dnum = node, dmax, dnum
    return dmax, dnum
  def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
    self.ans, self.dmax, self.dnum = root, 0, 1
    self.recursive(root, 0)
    return self.ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,2,3],
    [1,2,3,4],
    [1,2,3,4,5],
    [1,None,2,3],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.lcaDeepestLeaves(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution:\n{rs}")
