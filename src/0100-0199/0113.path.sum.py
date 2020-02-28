from typing import List
from config.treenode import TreeNode, listToTreeNode


class Solution:
  def recursive(self, ans, rslt, node, val):
    if node.left is None and node.right is None:
      if node.val == val:
        ans.append(rslt + [node.val])
    if node.left is not None:
      self.recursive(ans, rslt + [node.val], node.left, val - node.val)
    if node.right is not None:
      self.recursive(ans, rslt + [node.val], node.right, val - node.val)
  def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    x = []
    if root is not None:
      self.recursive(x, [], root, sum)
    return x


class Solution:
  def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    """Iterative, DFS or BFS.
    """
    x, stack = [], [(root, sum, []), ]
    if root is not None:
      while stack:
        node, val, rslt = stack.pop()
        if node.left is None and node.right is None and node.val == val:
          x.append(rslt + [node.val])
        if node.right is not None:
          stack.append((node.right, val - node.val, rslt + [node.val]))
        if node.left is not None:
          stack.append((node.left, val - node.val, rslt + [node.val]))
    return x


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # ([], 0), # false
    # ([], 1), # false
    # ([], -1), # false
    ([1, 2], 1),
    ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22),
    ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22),
  ]
  cases = [
    (listToTreeNode(x), val) for x, val in cases
  ]
  rslts = [
    solver.pathSum(x, val) for x, val in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display()}\n{cs[1]}, solution: {rs}")