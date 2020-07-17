from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, depth, parent):
    if node.val == self.x:
      self.dp[0] = (depth, parent)
      if self.dp[1][0]:
        return None
    if node.val == self.y:
      self.dp[1] = (depth, parent)
      if self.dp[0][0]:
        return None
    if node.left:
      self.recursive(node.left, depth + 1, node.val)
    if node.right:
      self.recursive(node.right, depth + 1, node.val)
  def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    # dp: (depth, parent)
    self.dp = [(None, None), (None, None)]
    self.x, self.y = x, y
    self.recursive(root, 0, '')
    return self.dp[0][0] == self.dp[1][0] and self.dp[0][1] != self.dp[1][1]

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,None,2,3], 2, 3),
    ([1,2,3,None,4,None,5], 5, 4),
  ]
  cases = [
    (listToTreeNode(r), x, y) for r, x, y in cases
  ]
  rslts = [
    solver.isCousins(root, x, y) for root, x, y in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None}\n+{cs[1:]} | solution: {rs}")
