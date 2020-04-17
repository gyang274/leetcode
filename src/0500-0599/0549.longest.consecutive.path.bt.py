from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    il, dl = 1, 1
    if node.left:
      il, dl = self.recursive(node.left)
      if node.val == node.left.val + 1:
        il += 1
      else:
        il = 1
      if node.val == node.left.val - 1:
        dl += 1
      else:
        dl = 1
    ir, dr = 1, 1
    if node.right:
      ir, dr = self.recursive(node.right)
      if node.val == node.right.val + 1:
        ir += 1
      else:
        ir = 1
      if node.val == node.right.val - 1:
        dr += 1
      else:
        dr = 1
    self.xmax = max(self.xmax, il + dr - 1, dl + ir - 1)
    return max(il, ir), max(dl, dr)
  def longestConsecutive(self, root: TreeNode) -> int:
    self.xmax = 0
    if root:
      self.recursive(root)
    return self.xmax

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [1],
    [1,2,3],
    [2,1,3],
    [1,None,2,3],
    [3,None,4,None,1,None,2],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.longestConsecutive(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
