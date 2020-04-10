from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    xl, xr = 0, 0
    if node.left:
      xl = max(self.recursive(node.left)) + 1
    if node.right:
      xr = max(self.recursive(node.right)) + 1
    self.diameter = max(self.diameter, xl + xr)
    return xl, xr
  def diameterOfBinaryTree(self, root: TreeNode) -> int:
    self.diameter = 0
    if root:
      self.recursive(root)
    return self.diameter

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
    [1,2,3,4,5,None,None,6,None,7,None,8,None,None,9],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.diameterOfBinaryTree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
