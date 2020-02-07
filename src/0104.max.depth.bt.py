from config.treenode import TreeNode, listToTreeNode


class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    level, stack = 0, [(1, root), ]
    while stack:
      i, node = stack.pop()
      if node is not None:
        level = max(level, i)
        stack.append((i + 1, node.right))
        stack.append((i + 1, node.left))
    return level


class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    if root is None:
      return 0
    level, stack = 0, [(1, root), ]
    while stack:
      i, node = stack.pop()
      level = max(level, i)
      if node.right is not None:
        stack.append((i + 1, node.right))
      if node.left is not None:
        stack.append((i + 1, node.left))
    return level


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1, None, 2, 3],
    [1,2,3,4,None,None,5],
    [3,9,20,None,None,15,7],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.maxDepth(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")