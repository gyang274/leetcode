from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, x):
    x = (x << 1) | node.val
    if node.left or node.right:
      if node.left:
        self.recursive(node.left, x)
      if node.right:
        self.recursive(node.right, x)
    else:
      self.s += x
  def sumRootToLeaf(self, root: TreeNode) -> int:
    self.s = 0
    self.recursive(root, 0)
    return self.s
    
if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,0,1,0,1,0,1],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.sumRootToLeaf(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
