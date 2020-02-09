from config.treenode import TreeNode, listToTreeNode

class Solution:
  def sumNumbers(self, root: TreeNode) -> int:
    """any order (preorder, inorder, postorder) traversal, accumlate sum at leaf.
    """
    x = 0
    if root is not None:
      stack = [(root, str(root.val)), ]
      while stack:
        node, num = stack.pop()
        if node.right is None and node.left is None:
          x += int(num)
        if node.right is not None:
          stack.append((node.right, num + str(node.right.val)))
        if node.left is not None:
          stack.append((node.left, num + str(node.left.val)))
    return x

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1, 2, 3],
    [2, 1, 3],
    [1, None, 2, 3],
    [3,9,20,None,None,15,7],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.sumNumbers(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")