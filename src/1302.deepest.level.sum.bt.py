from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, depth):
    if node.left or node.right:
      if node.left:
        self.recursive(node.left, depth + 1)
      if node.right:
        self.recursive(node.right, depth + 1)
    else:
      if depth == self.dmax:
        self.xsum += node.val
      elif depth > self.dmax:
        self.dmax, self.xsum = depth, node.val
  def deepestLeavesSum(self, root: TreeNode) -> int:
    self.dmax, self.xsum = -1, 0
    self.recursive(root, 0)
    return self.xsum

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
    [1,2,3,4,5,None,6,7,None,None,None,None,8],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.deepestLeavesSum(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
