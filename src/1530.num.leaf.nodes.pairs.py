from config.treenode import TreeNode, listToTreeNode

from collections import defaultdict

class Solution:
  def recursive(self, node):
    if not (node.left or node.right):
      return {1: 1}
    dl, dr = {}, {}
    if node.left:
      dl = self.recursive(node.left)
    if node.right:
      dr = self.recursive(node.right)
    for x in dl:
      for y in dr:
        if x + y <= self.z:
          self.count += dl[x] * dr[y]
    d = defaultdict(lambda: 0)
    for x in dl:
      if x + 1 < self.z:
        d[x + 1] += dl[x]
    for x in dr:
      if x + 1 < self.z:
        d[x + 1] += dr[x]
    return d
  def countPairs(self, root: TreeNode, distance: int) -> int:
    self.count, self.z = 0, distance
    self.recursive(root)
    return self.count

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,2,3,4,5], 3),
  ]
  cases = [
    (listToTreeNode(x), d) for x, d in cases
  ]
  rslts = [
    solver.countPairs(root, distance) for root, distance in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None} + {cs[1:]} | solution: {rs}")
