from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, path, node):
    path.append(0)
    for i in range(len(path)):
      path[i] += node.val
      if path[i] == self.sum:
        self.ans += 1
    if node.left:
      self.recursive(path.copy(), node.left)
    if node.right:
      self.recursive(path.copy(), node.right)
    return None
  def pathSum(self, root: TreeNode, sum: int) -> int:
    self.ans, self.sum = 0, sum
    if root:
      self.recursive([], root)
    return self.ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([], 0),
    ([], 1),
    ([0], 0),
    ([1], 1),
    ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22),
  ]
  cases = [
    (listToTreeNode(x), s) for x, s in cases
  ]
  rslts = [
    solver.pathSum(root, sum) for root, sum in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None} - {cs[1]}, solution: {rs}")