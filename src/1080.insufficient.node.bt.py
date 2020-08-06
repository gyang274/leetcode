from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, x):
    x += node.val
    if node.left or node.right:
      sL = False
      if node.left:
        # sufficient on any left
        sL = self.recursive(node.left, x)
        if not sL:
          node.left = None
      sR = False
      if node.right:
        # sufficient on any left
        sR = self.recursive(node.right, x)
        if not sR:
          node.right = None
      return sL or sR
    else:
      # leaf node
      return x >= self.limit
  def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
    self.limit = limit
    # node is insufficient iff all sub-nodes are insufficient
    ss = self.recursive(root, 0)
    return root if ss else None

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,None,2,3], 4),
    ([1,None,2,3], 7),
    ([5,4,8,11,None,17,4,7,1,None,None,5,3], 22),
  ]
  cases = [
    (listToTreeNode(x), limit) for x, limit in cases
  ]
  rslts = [
    solver.sufficientSubset(root, limit) for root, limit in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None} + {cs[1]}\nsolution:\n{rs.display() if rs else None}")
