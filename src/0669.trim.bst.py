from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    if not node:
      return node
    while node and (node.val < self.L or node.val > self.R):
      if node.val < self.L:
        node = node.right
      else:
        # node.val > self.R:
        node = node.left
    if node:
      node.left = self.recursive(node.left)
      node.right = self.recursive(node.right)
    return node
  def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
    self.L, self.R = L, R
    return self.recursive(root)

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,None,2,3], 1, 2),
    ([3,0,4,None,1,None,None,2], 1, 3),
    ([3,0,4,None,1,None,None,2], 2, 4),
  ]
  cases = [
    (listToTreeNode(x), L, R) for x, L, R in cases
  ]
  rslts = [
    solver.trimBST(root, L, R) for root, L, R in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs else None} + {cs[1:]}\nsolution:\n{rs.display() if rs else None}")
