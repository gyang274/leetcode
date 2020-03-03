from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    if node.left is not None:
      self.recursive(node.left)
    if node.right is not None:
      self.recursive(node.right)
    node.unix = True
    node.unix &= (node.left is None) or (node.left.unix and node.left.val == node.val)
    node.unix &= (node.right is None) or (node.right.unix and node.right.val == node.val)
    if node.unix:
      self.count += 1
  def countUnivalSubtrees(self, root: TreeNode) -> int:
    """postorder traversal, (left, right, root)
     subtree rooted at node is univalue if (left is None or (left is univalue and node.left.val == node.val) and 
        (right is None or (right is univalue and node.right.val == node.val)
    """
    self.count = 0
    if root:
      self.recursive(root)
    return self.count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [5,1,5,5,5,None,5],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [solver.countUnivalSubtrees(root) for root in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()} | solution: {rs}")