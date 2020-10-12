from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, pr, pp):
    if pp ^ 1:
      self.x += node.val
    if node.left:
      self.recursive(node.left, node.val & 1, pr)
    if node.right:
      self.recursive(node.right, node.val & 1, pr)
  def sumEvenGrandparent(self, root: TreeNode) -> int:
    self.x = 0
    self.recursive(root, 1, 1)
    return self.x

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [2,None,1,3],
    [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.sumEvenGrandparent(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
