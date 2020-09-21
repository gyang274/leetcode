class FindElements:

  def __init__(self, root: TreeNode):
    self.vals = set()
    # recover the binary tree
    def recursive(node):
      self.vals.add(node.val)
      if node.left:
        node.left.val = 2 * node.val + 1
        recursive(node.left)
      if node.right:
        node.right.val = 2 * node.val + 2
        recursive(node.right)
    root.val = 0
    recursive(root)

  def find(self, target: int) -> bool:
    return target in self.vals
