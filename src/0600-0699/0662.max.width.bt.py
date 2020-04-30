from config.treenode import TreeNode, listToTreeNode

class Solution:
  def widthOfBinaryTree(self, root: TreeNode) -> int:
    if not root:
      return 0
    queue, width = [(root, 0)], 0
    while queue:
      width = max(width, queue[-1][1] - queue[0][1] + 1)
      qnext = []
      for node, index in queue:
        if node.left:
          qnext.append((node.left, index * 2))
        if node.right:
          qnext.append((node.right, index * 2 + 1))
      queue = qnext
    return width

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.widthOfBinaryTree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
