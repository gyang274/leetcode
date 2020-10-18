from typing import List
from config.treenode import TreeNode, listToTreeNode

import itertools

class Solution:
  def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
    queue = [root]
    for x in arr:
      if not queue:
        return False
      queue = list(
        itertools.chain.from_iterable(
          (node.left, node.right) for node in queue if node and node.val == x
        )
      )
    for l, r in zip(queue[::2], queue[1::2]):
      if not (l or r):
        return True
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([8,3,None,2,1,5,4], [8]),
    ([0,1,0,0,1,0,None,None,1,0,0], [0,0,1]),
    ([0,1,0,0,1,0,None,None,1,0,0], [0,1,1]),
    ([0,1,0,0,1,0,None,None,1,0,0], [0,1,0,1]),
  ]
  cases = [
    (listToTreeNode(x), arr) for x, arr in cases
  ]
  rslts = [
    solver.isValidSequence(root, arr) for root, arr in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None} + {cs[1:]} | solution: {rs}")
