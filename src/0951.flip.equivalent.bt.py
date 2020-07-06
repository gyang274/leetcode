from config.treenode import TreeNode, listToTreeNode

class Solution:
  def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
    if not root1 and not root2:
      return True
    if root1 and root2 and root1.val == root2.val:
      return (
        self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
      ) or (
        self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
      )
    return False

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,2,3,4,5,6,None,None,None,7,8], [1,3,2,None,6,4,5,None,None,None,None,8,7]),
  ]
  cases = [
    (listToTreeNode(x1), listToTreeNode(x2)) for x1, x2 in cases
  ]
  rslts = [
    solver.flipEquiv(root1, root2) for root1, root2 in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None}\n+\n{cs[1].display() if cs[1] else None}\n| solution: {rs}")
