from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursiveSum(self, node):
    xl = self.recursiveSum(node.left) if node.left else 0
    xr = self.recursiveSum(node.right) if node.right else 0
    node.sum = node.val + xl + xr
    return node.sum
  def recursiveProd(self, node):
    # prod if split by this node - node's parent
    self.pmax = max(self.pmax, node.sum * (self.xsum - node.sum))
    if node.left:
      self.recursiveProd(node.left)
    if node.right:
      self.recursiveProd(node.right)
    return None
  def maxProduct(self, root: TreeNode) -> int:
    self.xsum, self.pmax = self.recursiveSum(root), 0
    self.recursiveProd(root)
    return self.pmax % (10 ** 9 + 7)

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
    [1,2,3,4,5,6],
    [1,None,2,3,4,None,None,5,6]
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.maxProduct(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
