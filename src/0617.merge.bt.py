from config.treenode import TreeNode, listToTreeNode

class Solution:
  def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 and t2:
      t = TreeNode(t1.val + t2.val)
      t.left = self.mergeTrees(t1.left, t2.left)
      t.right = self.mergeTrees(t1.right, t2.right)
    elif t1:
      t = t1
    elif t2:
      t = t2
    else:
      t = None
    return t

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,3,2,5], [2,1,3,None,4,None,7]),
  ]
  cases = [
    (listToTreeNode(x1), listToTreeNode(x2)) for x1, x2 in cases
  ]
  rslts = [
    solver.mergeTrees(t1, t2) for t1, t2 in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None} +\n{cs[1].display() if cs[1] else None} | solution:\n{rs.display() if rs else None}")

