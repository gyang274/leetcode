from config.treenode import TreeNode, listToTreeNode


class Solution:
  def recursive(self, node):
    node.dl = 0 if node.left is None else (1 + max(self.recursive(node.left)))
    node.dr = 0 if node.right is None else (1 + max(self.recursive(node.right)))
    self.balance &= abs(node.dl - node.dr) <= 1
    return (node.dl, node.dr)
  def isBalanced(self, root: TreeNode) -> bool:
    if not root:
      return True
    # recursive on depth left and right, following postorder traversal
    self.balance = True
    self.recursive(root)
    return self.balance


class Solution:
  def recursive(self, node):
    node.dl = 0 if node.left is None else (1 + max(self.recursive(node.left)))
    node.dr = 0 if node.right is None else (1 + max(self.recursive(node.right)))
    self.balance &= abs(node.dl - node.dr) <= 1
    if not self.balance:
      raise ValueError()
    return (node.dl, node.dr)
  def isBalanced(self, root: TreeNode) -> bool:
    """Early break: simulate break out of loop through try catch.
    """
    if not root:
      return True
    # recursive on depth left and right, following postorder traversal
    self.balance = True
    try:
      self.recursive(root)
    except ValueError:
      return self.balance
    return self.balance


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1,None,3,2],
    [3,9,20,None,None,15,7],
    [1,2,2,3,3,None,None,4,4],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.isBalanced(nums) for nums in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")