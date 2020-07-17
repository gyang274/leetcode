from config.treenode import TreeNode, listToTreeNode

class Solution:
  def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
    # Q0654.
    if not root or root.val < val:
      node = TreeNode(val)
      node.left = root
      return node
    else:
      root.right = self.insertIntoMaxTree(root.right, val)
      return root

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([5,2,4,None,1], 3),
    ([5,2,3,None,1], 4),
    ([4,1,3,None,None,2], 5),
  ]
  cases = [
    (listToTreeNode(x), val) for x, val in cases
  ]
  rslts = [
    solver.insertIntoMaxTree(root, val) for root, val in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs else None}\n+{cs[1:]} | solution:\n{rs.display() if rs else None}")
