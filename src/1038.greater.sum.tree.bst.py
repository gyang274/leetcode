from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node, val):
    node.val += self.recursive(node.right, val) if node.right else val
    return self.recursive(node.left, node.val) if node.left else node.val
  def bstToGst(self, root: TreeNode) -> TreeNode:
    self.recursive(root, 0)
    return root

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.bstToGst(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None}\nsolution:\n{rs.display() if rs else None}")
