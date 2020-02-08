from config.treenode import TreeNode, listToTreeNode


class Solution:
  def flatten(self, root: TreeNode) -> None:
    """Do not return anything, modify root in-place instead.
    """
    if root is None:
      return None
    node, stack = root, []
    while node is not None or stack:
      if node.left is not None and node.right is not None:
        stack.append(node.right)
        node.right = node.left
        node.left = None
      elif node.left is not None:
        node.right = node.left
        node.left = None
      elif node.right is not None:
        pass
      elif stack:
        node.right = stack.pop()
      node = node.right  
    return None


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1, None, 2, 3],
    [1,2,3,4,None,None,5],
    [3,9,20,None,None,15,7],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.flatten(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")