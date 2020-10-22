from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, x):
    if node.val >= x:
      self.count += 1
      x = node.val
    if node.left:
      self.recursive(node.left, x)
    if node.right:
      self.recursive(node.right, x)
  def goodNodes(self, root: TreeNode) -> int:
    self.count = 0
    self.recursive(root, float('-inf'))
    return self.count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [3,1,4,3,None,1,5],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.goodNodes(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
