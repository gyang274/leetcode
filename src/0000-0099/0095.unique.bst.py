from typing import List
from config.treenode import TreeNode

class Solution:
  def preorderListToTreeNode(self, x: List) -> TreeNode:
    """preorder representation of tree as list with none back to root (TreeNode), copied from ./config/treenode.py
    """
    if not x:
      return None
    root = TreeNode(x[0])
    i, q = 1, [[root, True], ]
    while i < len(x):
      node, ld = q[-1]
      item = x[i]
      if ld:
        q[-1][1] = False
        if item is not None:
          node.left = TreeNode(item)
          q.append([node.left, True])
      else:
        q.pop()
        if item is not None:
          node.right = TreeNode(item)
          q.append([node.right, True])
      i += 1
    return root
  def generateTrees(self, n: int) -> List[TreeNode]:
    if n == 0:
      return []
    # use memo to store intermedidate tree represented by list
    memo = {}
    memo[0] = [[None]]
    memo[1] = [[1, None, None]]
    for i in range(2, n + 1):
      memo[i] = []
      for j in range(i):
        for l in memo[j]:
          for r in memo[i - 1 -j]:
            memo[i].append(
              [j + 1] + l + [x + j + 1 if x is not None else None for x in r]
            )
    # convert list to root treenode
    ans = [self.preorderListToTreeNode(x) for x in memo[n]]
    return ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    0,
    1,
    2,
    3,
    4,
    5,
  ]
  rslts = [
    solver.generateTrees(n) for (n) in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {len(rs)}")
    for r in rs:
      print(r.display())
