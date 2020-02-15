from config.treenode import TreeNode, listToTreeNode

class Solution:
  def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
    s = x = root
    if root is not None:
      stack = []
      while x.left is not None:
        stack.append(x)
        x = x.left
      s = x
      while stack:
        y = stack.pop()
        y.left = None
        x.left = y.right
        y.right = None
        x.right = y
        x = x.right
    return s

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6, 7],
    [1,2,3,4,5,6,7,8,9,None,None,10,11],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.upsideDownBinaryTree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution:\n{rs.display()}")