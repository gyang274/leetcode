from config.treenode import TreeNode, listToTreeNode


class Solution:
  def isSymmetric(self, root: TreeNode) -> bool:
    if root is None or (root.left is None and root.right is None):
      return True
    # stack of root left nodes, stack of root right nodes
    sl, sr = [root.left, ], [root.right, ]
    while sl or sr:
      nl, nr = sl.pop(), sr.pop()
      if nl is not None and nr is not None:
        if nl.val == nr.val:
          sl.extend((nl.right, nl.left))
          sr.extend((nr.left, nr.right))
        else:
          return False
      if (nl is None and nr is not None) or (nl is not None and nr is None):
        return False
    return True


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,2,2,3,4,4,3],
    [1,2,2,None,3,None,3],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.isSymmetric(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")