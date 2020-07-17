from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    uL = self.recursive(node.left) if node.left else True
    if not uL:
      return False
    uR = self.recursive(node.right) if node.right else True
    if not uR:
      return False
    return node.val == self.root.val
  def isUnivalTree(self, root: TreeNode) -> bool:
    self.root = root
    return self.recursive(root)

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [0],
    [0,0,None,0,0],
    [1,1,1,1,1,None,1],
    [2,2,2,2,5,None,2],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.isUnivalTree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
