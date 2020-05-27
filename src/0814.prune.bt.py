from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    l = 0
    if node.left:
      l = self.recursive(node.left)
      if not l:
        node.left = None
    r = 0
    if node.right:
      r = self.recursive(node.right)
      if not r:
        node.right = None
    return node.val + l + r
  def pruneTree(self, root: TreeNode) -> TreeNode:
    if root:
      x = self.recursive(root)
      if not x:
        root = None
    return root

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [0],
    [1],
    [1,None,0,0,1],
    [1,0,1,0,0,0,1],
    [1,1,0,1,1,0,1,0],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.pruneTree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None}\nsolution:\n{rs.display() if rs else None}")
