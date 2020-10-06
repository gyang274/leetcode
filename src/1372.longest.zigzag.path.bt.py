from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, lr):
    if node.left:
      self.recursive(node.left, (lr[1] + 1, 0))
    else:
      self.zmax = max(self.zmax, lr[1])
    if node.right:
      self.recursive(node.right, (0, lr[0] + 1))
    else:
      self.zmax = max(self.zmax, lr[0])
  def longestZigZag(self, root: TreeNode) -> int:
    self.zmax = 0
    self.recursive(root, (0, 0))
    return self.zmax

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1],
    [1,1,1],
    [1,1,1,None,1,None,None,1,1,None,1],
    [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1,None,1],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.longestZigZag(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
