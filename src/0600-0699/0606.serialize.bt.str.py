class Solution:
  def tree2str(self, t: TreeNode) -> str:
    s = ""
    if t:
      s += str(t.val)
      if t.left:
        s += "(" + self.tree2str(t.left) + ")"
      if t.right:
        if not t.left:
          s += "()"
        s += "(" + self.tree2str(t.right) + ")"
    return s
