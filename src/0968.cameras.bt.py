from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    if node.left:
      self.recursive(node.left)
    if node.right:
      self.recursive(node.right)
    node.mnt = 1 if (node.left and node.left.val == 1) or (node.right and node.right.val == 1) else 0
    node.val = 1 if (node.left and node.left.val == 0 and node.left.mnt == 0) or (node.right and node.right.val == 0 and node.right.mnt == 0) else 0
    self.count += node.val
  def minCameraCover(self, root: TreeNode) -> int:
    self.count = 0
    self.recursive(root)
    if root.val == root.mnt == 0:
      root.val = 1
      self.count += 1
    return self.count

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [0],
    [0,0,None,0,0],
    [0,None,0,None,0,None,0],
    [0,0,0,None,None,None,0],
    [0,0,None,0,None,0,None,None,0],
    [0,0,None,None,0,0,None,None,0,0],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.minCameraCover(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
