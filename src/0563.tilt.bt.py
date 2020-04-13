class Solution:
  def recursive(self, node):
    xl, xr = 0, 0
    if node.left:
      xl = self.recursive(node.left)
    if node.right:
      xr = self.recursive(node.right)
    self.tilt += abs(xl - xr)
    return xl + xr + node.val
  def findTilt(self, root: TreeNode) -> int:
    self.tilt = 0
    if root:
      self.recursive(root)
    return self.tilt