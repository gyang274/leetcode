from config.treenode import TreeNode, listToTreeNode

class Solution:
  def isValidBST(self, root: TreeNode) -> bool:
    """Approaches:
      1. Recursive
      2. Iterative
      3. Inorder traversal leads to a sorted list.
    """
    if root is not None:
      x, node, stack = float('-inf'), root, []
      while node or stack:
        while node:
          stack.append(node)
          node = node.left
        node = stack.pop()
        if x < node.val:
          x = node.val
          node = node.right
        else:
          return False
    return True

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [1],
    [2, 1, 3],
    [1, None, 2, 3],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.isValidBST(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs is not None else cs}, solution: {rs}")