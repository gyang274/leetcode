class Solution:
  def averageOfLevels(self, root: TreeNode) -> List[float]:
    x = []
    if root:
      queue = [root]
      while queue:
        v, stack = 0, []
        for node in queue:
          v += node.val
          if node.left:
            stack.append(node.left)
          if node.right:
            stack.append(node.right)
        x.append(v / len(queue))
        queue = stack
    return x
