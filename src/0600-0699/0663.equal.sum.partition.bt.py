from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    xl = self.recursive(node.left) if node.left else 0
    xr = self.recursive(node.right) if node.right else 0
    xs = xl + xr + node.val
    # in case xs == 0 and node is root..
    if node is not self.root:
      self.xsum.add(xs)
    return xs
  def checkEqualTree(self, root: TreeNode) -> bool:
    self.root = root
    # xsum: subtree sum
    self.xsum = set([])
    s = self.recursive(root)
    return (s & 1 == 0) and (s // 2 in self.xsum)

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [0,-1,1],
    [1,None,2,3],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.checkEqualTree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
