from config.treenode import TreeNode, listToTreeNode


class Solution:
  def recursive(self, node):
    if node.left is not None or node.right is not None:
      # default to MAX_INTEGER
      node.depth = 2147483647
      if node.left is not None:
        node.depth = min(node.depth, 1 + self.recursive(node.left))
      if node.right is not None:
        node.depth = min(node.depth, 1 + self.recursive(node.right))
      return node.depth
    return 1
  def minDepth(self, root: TreeNode) -> int:
    if not root:
      return 0
    # recursive on depth left and right, following postorder traversal
    return self.recursive(root)


class Solution:
  def minDepth(self, root: TreeNode) -> int:
    """BFS: visit tree by level, first level with leaf node can break and return.
    """
    if not root:
      return 0
    level, stack, holds = 1, [root, ], []
    while stack or holds:
      if stack:
        node = stack.pop()
        if node.left is None and node.right is None:
          return level
        if node.right is not None:
          holds.append(node.right)
        if node.left is not None:
          holds.append(node.left)
      else:
        stack, holds = holds, stack
        level += 1
    return level



if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1,2],
    [1,None,3,2],
    [3,9,20,None,None,15,7],
    [1,2,2,3,3,None,None,4,4],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.minDepth(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")