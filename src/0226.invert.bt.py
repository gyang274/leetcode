from config.treenode import TreeNode, listToTreeNode

class Solution:
  def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
      stack = [root, ]
      while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
          stack.append(node.left)
        if node.right:
          stack.append(node.right)
    return root

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1,None,2,3],
    [4,2,7,1,3,6,9],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.invertTree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution:\n{rs.display()}")  