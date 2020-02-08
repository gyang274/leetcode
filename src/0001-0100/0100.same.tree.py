from config.treenode import TreeNode, listToTreeNode


class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    """Recursive.
    """
    if p is None and q is None:
      return True
    elif p is None or q is None or not p.val == q.val:
      return False
    else:
      return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    """Iterative.
    """
    if p is not None or q is not None:
      stack = [(p, q), ]
      while stack:
        p, q = stack.pop()
        if p is None and q is None:
          continue
        elif p is None or q is None or not p.val == q.val:
          return False
        else:
          stack.append((p.right, q.right))
          stack.append((p.left, q.left))
    return True


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2], [1, None, 2]),
    ([1, 2, 1], [1, 1, 2]),
  ]
  cases = [
    (listToTreeNode(x), listToTreeNode(y)) for x, y in cases
  ]
  rslts = [
    solver.isSameTree(p, q) for p, q in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display()}\n{cs[1].display()}, solution: {rs}")