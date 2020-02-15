from config.treenode import TreeNode, listToTreeNode

class BSTIterator:
  """inorder traversal leads to sorted array.
  """
  def __init__(self, root: TreeNode):
    self.nums = []
    node, stack = root, [ ]
    while node is not None or stack:
      while node is not None:
        stack.append(node)
        node = node.left
      node = stack.pop()
      self.nums.append(node.val)
      node = node.right
    # next and hasNext
    self.i, self.n = -1, len(self.nums)

  def next(self) -> int:
    """@return the next smallest number
    """
    self.i += 1
    return self.nums[self.i]
        
  def hasNext(self) -> bool:
    """@return whether we have a next smallest number
    """
    return self.i + 1 < self.n
        
class BSTIterator:
  """controlled recursion.
    This like split the work of inorder traversal into when it is necessary.
  """
  def __init__(self, root: TreeNode):
    self.stack = []
    self._leftmost_inorder(root)
  
  def _leftmost_inorder(self, root):
    while root is not None:
      self.stack.append(root)
      root = root.left

  def next(self) -> int:
    """@return the next smallest number
    """
    node = self.stack.pop()
    if node.right is not None:
      self._leftmost_inorder(node.right)
    return node.val
        
  def hasNext(self) -> bool:
    """@return whether we have a next smallest number
    """
    return len(self.stack) > 0
