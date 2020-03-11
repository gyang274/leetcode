from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node: TreeNode):
    """recursive over tree, return True/False, size, min, max if isBST.
    """
    if not node:
      return True, 0, None, None
    okl, nl, minl, maxl = self.recursive(node.left)
    okr, nr, minr, maxr = self.recursive(node.right)
    if (okl and okr):
      xmin, xmax = node.val, node.val
      if node.left:
        if node.val > maxl:
          xmin = minl
        else:
          return False, max(nl, nr), None, None        
      if node.right:
        if node.val < minr:
          xmax = maxr
        else:
          return False, max(nl, nr), None, None
      return True, 1 + (nl + nr), xmin, xmax
    else:
      return False, max(nl, nr), None, None
  def largestBSTSubtree(self, root: TreeNode) -> int:
    ok, n, xmin, xmax = self.recursive(root)
    return n

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [1,None,2,3],
    [3,2,4,None,None,1],
    [9,5,11,1,8,None,7],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.largestBSTSubtree(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")