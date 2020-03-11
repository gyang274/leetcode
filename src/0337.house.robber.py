from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node: TreeNode, robable: bool) -> int:
    """Args
      robable: can this node be robbed or not.
    """
    if not node:
      return 0
    # option 1: don't rob this one, then any of its children can be robbed.
    x = self.recursive(node.left, True) + self.recursive(node.right, True)
    if robable:
      # option 2: rob this one, then neither of its children can be robbed.
      x = max(x, node.val + self.recursive(node.left, False) + self.recursive(node.right, False))
    return x
  def rob(self, root: TreeNode) -> int:
    return self.recursive(root, True)

class Solution:
  def recursive(self, node):
    if node.left:
      self.recursive(node.left)
    if node.right:
      self.recursive(node.right)
    # max value if rob this one
    node.robVal = node.val + (node.left.notVal if node.left else 0) + (node.right.notVal if node.right else 0)
    # max value if not rob this one
    node.notVal = (max(node.left.robVal, node.left.notVal) if node.left else 0) + (max(node.right.robVal, node.right.notVal) if node.right else 0)
  def rob(self, root: TreeNode) -> int:
    if not root:
      return 0
    self.recursive(root)
    return max(root.robVal, root.notVal)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [3],
    [3,2,3,None,3,None,1],
    [3,4,5,1,3,None,1],
    [3,4,5,None,None,6,7],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [solver.rob(root) for root in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")