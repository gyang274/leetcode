from config.treenode import TreeNode, listToTreeNode

class Solution:
  def preprocess(self, node):
    """augment TreeNode with depth = (dl, dr).
    """
    if not (node.left or node.right):
      node.depth = [[1, node.val], [1, node.val]]
    else:
      node.depth = [[float('inf'), None], [float('inf'), None]]
      if node.left:
        node.depth[0] = min(self.preprocess(node.left))
        node.depth[0][0] += 1
      if node.right:
        node.depth[1] = min(self.preprocess(node.right))
        node.depth[1][0] += 1
    return node.depth
  def recursive(self, dp, node):
    # dp: min depth to leaf via parent, leaf value
    if node.val == self.k:
      return True, min(dp, *node.depth)[1]
    else:
      if node.left:
        found, leafval = self.recursive([node.depth[1][0] + 1, node.depth[1][1]], node.left)
        if found:
          return found, leafval
      if node.right:
        found, leafval = self.recursive([node.depth[0][0] + 1, node.depth[0][1]], node.right)
        if found:
          return found, leafval
      return False, None
  def findClosestLeaf(self, root: TreeNode, k: int) -> int:
    self.k = k
    self.preprocess(root)
    return self.recursive([float('inf'), None], root)[1]

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1], 1),
    ([1,None,2,3], 2),
    ([1,2,3,4,None,None,None,5,None,6], 2),
    ([1,2,3,None,None,4,5,6,None,None,7,8,9,10], 7),
  ]
  cases = [
    (listToTreeNode(x), k) for x, k in cases
  ]
  rslts = [
    solver.findClosestLeaf(root, k) for root, k in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs else None}, {cs[1:]} | solution: {rs}")
