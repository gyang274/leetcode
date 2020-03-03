from config.treenode import TreeNode, listToTreeNode

class Solution:
  def backtrack(self, x, node):
    """x: length of consecutive path to this node.
    """
    self.xmax = max(self.xmax, x)
    if node.left:
      xleft = (x + 1) if node.left.val == node.val + 1 else 1
      self.backtrack(xleft, node.left)
    if node.right:
      xright = (x + 1) if node.right.val == node.val + 1 else 1
      self.backtrack(xright, node.right)
  def longestConsecutive(self, root: TreeNode) -> int:
    """DFS
    """
    self.xmax = 0
    if root:
      self.backtrack(1, root)
    return self.xmax

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [1],
    [1,None,2,3],
    [1,None,3,2,4,None,None,None,5],
    [2,None,3,1,4,None,None,None,5],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.longestConsecutive(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")       