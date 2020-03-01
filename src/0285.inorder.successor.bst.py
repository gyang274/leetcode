from config.treenode import TreeNode, listToTreeNode

class Solution:
  def _nextGT(self, stack):
    """find node with smallest value > stack[-1].val.
    """
    if stack:
      node = stack.pop()
      # partial inorder: (left, root, right)
      if node.right:
        node = node.right
        stack.append(node)
        while node.left:
          node = node.left
          stack.append(node)
      else:
        while stack and stack[-1].val < node.val:
          stack.pop()
      return stack[-1] if stack else None
    return None
  def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
    """Q0272, inorder predecessor and successor.
    """
    # stack from root to p
    node, stack = root, []
    while node:
      stack.append(node)
      if node is p:
        break
      elif p.val < node.val:
        node = node.left
      else:
        node = node.right
    return self._nextGT(stack)
