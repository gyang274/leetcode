from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    # node
    if node.val < self.min1:
      self.min1, self.min2 = node.val, self.min1
    elif self.min1 < node.val < self.min2:
      self.min2 = node.val
    # node left and node right
    if node.left and node.right:
      if node.left.val < node.right.val:
        if node.right.val < self.min2:
          self.min2 = node.right.val
        self.recursive(node.left)
      elif node.left.val > node.right.val:
        if node.left.val < self.min2:
          self.min2 = node.left.val
        self.recursive(node.left)
      else:
        # node.left.val == node.right.val
        self.recursive(node.left)
        self.recursive(node.right)
  def findSecondMinimumValue(self, root: TreeNode) -> int:
    self.min1, self.min2 = float("inf"), float("inf")
    self.recursive(root)
    return -1 if self.min2 == float("inf") else self.min2

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [2,2,2],
    [5,8,5],
    [2,2,5,None,None,5,7],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.findSecondMinimumValue(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")

