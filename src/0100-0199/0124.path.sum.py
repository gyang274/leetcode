from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    hold_left, hold_right = 0, 0
    if node.left is not None:
      hold_left = max(0, self.recursive(node.left))
    if node.right is not None:
      hold_right = max(0, self.recursive(node.right))
    node.gain = node.val + max(0, hold_left, hold_right)
    node.sums = node.val + max(0, hold_left + hold_right)
    self.smax = max(self.smax, node.sums)
    return node.gain
  def maxPathSum(self, root: TreeNode) -> int:
    if not root:
      return 0
    self.smax = -2147483648
    self.recursive(root)
    return self.smax

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1,3,2],
    [1,-2,3],
    # [1,None,3,2],
    # [3,9,20,None,None,15,7],
    # [1,2,2,3,3,None,None,4,4],
    # [-10,9,20,None,None,15,7],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.maxPathSum(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")