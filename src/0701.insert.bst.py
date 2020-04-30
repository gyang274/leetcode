from config.treenode import TreeNode, listToTreeNode

class Solution:
  def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    if not root:
      return TreeNode(val)
    if root.val > val:
      root.left = self.insertIntoBST(root.left, val)
    else:
      root.right = self.insertIntoBST(root.right, val)
    return root
 
if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([5,3,7,2,4], 6),
  ]
  cases = [
    (listToTreeNode(x), val) for x, val in cases
  ]
  rslts = [
    solver.insertIntoBST(root, val) for root, val in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs else None} + {cs[1:]}\nsolution:\n{rs.display() if rs else None}")
