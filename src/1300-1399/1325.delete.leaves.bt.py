from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    if node.left:
      node.left = self.recursive(node.left)
    if node.right:
      node.right = self.recursive(node.right)
    if (node.left is None) and (node.right is None) and node.val == self.target:
      return None
    return node    
  def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
    self.target = target
    return self.recursive(root)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,1,1], 1),
    ([1,2,3,4], 2),
    ([1,3,3,3,2], 3),
    ([1,2,3,2,None,2,4], 2),
    ([1,2,None,2,None,2], 2),
  ]
  cases = [
    (listToTreeNode(x), target) for x, target in cases
  ]
  rslts = [
    solver.removeLeafNodes(root, target) for root, target in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None} + {cs[1:]}\nsolution:\n{rs.display() if rs else None}")
