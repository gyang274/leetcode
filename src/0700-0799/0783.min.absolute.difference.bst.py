from config.treenode import TreeNode, listToTreeNode

class Solution:
  def minDiffInBST(self, root: TreeNode) -> int:
    """Q0530, O(N), inorder traversal.
    """
    prev, xmin = float('-inf'), float('inf')
    node, stack = root, []
    while node or stack:
      while node:
        stack.append(node)
        node = node.left
      node = stack.pop()
      xmin = min(node.val - prev, xmin)
      prev = node.val
      node = node.right
    return xmin

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,None,3],
    [4,2,7,1,3,None,None],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.minDiffInBST(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
