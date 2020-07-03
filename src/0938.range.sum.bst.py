from config.treenode import TreeNode, listToTreeNode

class Solution:
  def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    if not root:
      return 0
    x = root.val
    if x > R:
      return self.rangeSumBST(root.left, L, R)
    elif x < L:
      return self.rangeSumBST(root.right, L, R)
    else:
      return x + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([10,5,15,3,7,None,18], 7, 15),
    ([10,5,15,3,7,13,18,1,None,6], 6, 10),
  ]
  cases = [
    (listToTreeNode(x), L, R) for x, L, R in cases
  ]
  rslts = [
    solver.rangeSumBST(root, L, R) for root, L, R in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs else None}\n+ {cs[1:]} | solution: {rs}")