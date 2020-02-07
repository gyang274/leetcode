from typing import List
from config.treenode import TreeNode, listToTreeNode


class Solution:
  def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    """Exact copy of 0102, except return list(reversed(x)).
    """
    if root is None:
      return []
    stack, x = [(0, root), ], []
    while stack:
      level, node = stack.pop()
      while level >= len(x):
        x.append([])
      x[level].append(node.val)
      if node.right is not None:
        stack.append((level + 1, node.right))
      if node.left is not None:
        stack.append((level + 1, node.left))
    return list(reversed(x))


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1, None, 2, 3],
    [3,9,20,None,None,15,7],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.levelOrderBottom(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")
