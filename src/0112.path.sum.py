from config.treenode import TreeNode, listToTreeNode


class Solution:
  def recursive(self, node, val):
    if node.left is None and node.right is None:
      if node.val == val:
        self.anyPathSum |= True
      else:
        self.anyPathSum |= False
    if node.left is not None:
      self.recursive(node.left, val - node.val)
    if node.right is not None:
      self.recursive(node.right, val - node.val)
  def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if root is None:
      return False
    self.anyPathSum = False
    self.recursive(root, sum)
    return self.anyPathSum


class Solution:
  def recursive(self, node, val):
    if node.left is None and node.right is None:
      if node.val == val:
        raise ValueError()
    if node.left is not None:
      self.recursive(node.left, val - node.val)
    if node.right is not None:
      self.recursive(node.right, val - node.val)
  def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    """Early break: simulate break out of loop through try catch.
    """
    if root is None:
      return False
    try:
      self.recursive(root, sum)
    except ValueError:
      return True
    return False


class Solution:
  def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    """Iterative, DFS or BFS.
    """
    if root is None:
      return False
    stack = [(root, sum), ]
    while stack:
      node, val = stack.pop()
      if node.left is None and node.right is None and node.val == val:
        return True
      if node.right is not None:
        stack.append((node.right, val - node.val))
      if node.left is not None:
        stack.append((node.left, val - node.val))
    return False


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # ([], 0), # false
    # ([], 1), # false
    # ([], -1), # false
    ([1, 2], 1),
    ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22),
  ]
  cases = [
    (listToTreeNode(x), val) for x, val in cases
  ]
  rslts = [
    solver.hasPathSum(x, val) for x, val in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display()}\n{cs[1]}, solution: {rs}")