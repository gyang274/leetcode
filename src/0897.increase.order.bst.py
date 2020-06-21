class Solution:
  def increasingBST(self, root: TreeNode) -> TreeNode:
    # inorder traversal
    s = curr = TreeNode('')
    node, stack = root, []
    while node or stack:
      while node:
        stack.append(node)
        node = node.left
      node = stack.pop()
      curr.left = None
      curr.right = node
      curr = curr.right
      node = node.right
    return s.right
