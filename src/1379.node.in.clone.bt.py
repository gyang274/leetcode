class Solution:
  def recursive(self, node, clone):
    if node == self.target:
      self.copied = clone
    else:
      if node.left:
        self.recursive(node.left, clone.left)
      if node.right:
        self.recursive(node.right, clone.right)
  def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    # assume repeated value allowed
    self.copied, self.target = None, target
    self.recursive(original, cloned)
    return self.copied
