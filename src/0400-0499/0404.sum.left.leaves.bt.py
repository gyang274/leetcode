from config.treenode import TreeNode, listToTreeNode

class Solution:
  def sumOfLeftLeaves(self, root: TreeNode) -> int:
    if not root:
      return 0
    xsum, stack = 0, [(root, "r"), ]
    while stack:
      node, lr = stack.pop()
      if not node.left and not node.right:
        xsum += node.val if lr == "l" else 0
      else:
        if node.left:
          stack.append((node.left, "l"))
        if node.right:
          stack.append((node.right, "r"))
    return xsum

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
    [3,9,20,None,None,15,7]
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.sumOfLeftLeaves(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")