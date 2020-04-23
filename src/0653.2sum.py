class Solution:
  def recursive(self, node):
    if self.k - node.val in self.seen:
      return True
    self.seen.add(node.val)
    if node.right and self.recursive(node.right):
      return True
    if node.left and self.recursive(node.left):
      return True
    return False
  def findTarget(self, root: TreeNode, k: int) -> bool:
    self.seen, self.k = set([]), k
    return self.recursive(root)
    


        