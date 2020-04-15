class Solution:
  def sameTree(self, s, t):
    return (s is None and t is None) or (s and t and s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
  def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    return self.sameTree(s, t) or (s and (self.isSubtree(s.left, t) or self.isSubtree(s.right, t)))
