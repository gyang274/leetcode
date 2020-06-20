from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def __init__(self):
    self.memo = {}
    self.memo[1] = [TreeNode(0)]
  def allPossibleFBT(self, N: int) -> List[TreeNode]:
    if N & 1:
      if N not in self.memo:
        self.memo[N] = []
        for i in range(1, N, 2):
          for x in self.allPossibleFBT(i):
            for y in self.allPossibleFBT(N - 1 - i):
              node = TreeNode(0)
              node.left = x
              node.right = y
              self.memo[N].append(node)
      return self.memo[N]
    return []

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 13, 23
  ]
  rslts = [solver.allPossibleFBT(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")