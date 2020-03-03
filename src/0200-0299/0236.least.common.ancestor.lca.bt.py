class Solution:
  def dfs(self, path, root, node):
    path.append(root)
    if root is node:
      return True
    elif root.left and self.dfs(path, root.left, node):
      return True
    elif root.right and self.dfs(path, root.right, node):
      return True
    path.pop()
    return False
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    p_path = []
    self.dfs(p_path, root, p)
    while len(p_path) > 1:
      node = p_path.pop()
      if self.dfs([], node, q):
        return node
      # unlink the node to eliminate repeat search on the same sub-tree in next iteration.
      if p_path[-1].left is node:
        p_path[-1].left = None
      else:
        p_path[-1].right = None
    return root

class Solution:
  """backtrack.
  """
  def backtrack(self, path, root, nodes):
    """Keep track each node along the path: left sub-tree has p or q, itself is p or q, and right sub-tree has p or q.
    """
    path.append([root, False, False, False])
    if root in nodes:
      path[-1][2] = True
      nodes.remove(root)
      if not nodes:
        status = path.pop()
        return True, None
    if root.left:
      subtree_status = self.backtrack(path, root.left, nodes)
      if subtree_status[0]:
        path[-1][1] = True
      if not nodes:
        status = path.pop()
        if subtree_status[1] is not None:
          return True, subtree_status[1]
        elif sum(status[1:4]) == 2:
          return True, status[0]
        else:
          return True, None
    if root.right:
      subtree_status = self.backtrack(path, root.right, nodes)
      if subtree_status[0]:
        path[-1][3] = True
      if not nodes:
        status = path.pop()
        if subtree_status[1] is not None:
          return True, subtree_status[1]
        elif sum(status[1:4]) == 2:
          return True, status[0]
        else:
          return True, None
    status = path.pop()
    if sum(status[1:4]) == 1:
      return True, None
    return False, None
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    x = self.backtrack([], root, set([p, q]))
    return x[1]

class Solution:
  def __init__(self):
    # Variable to store LCA node.
    self.ans = None
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def recurse_tree(current_node):
      # If reached the end of a branch, return False.
      if not current_node:
        return False
      # Left Recursion
      left = recurse_tree(current_node.left)
      # Right Recursion
      right = recurse_tree(current_node.right)
      # If the current node is one of p or q
      mid = current_node == p or current_node == q
      # If any two of the three flags left, right or mid become True.
      if mid + left + right >= 2:
        self.ans = current_node
      # Return True if either of the three bool values is True.
      return mid or left or right
    # Traverse the tree
    recurse_tree(root)
    return self.ans

class Solution:
  def __init__(self):
    # Variable to store LCA node.
    self.ans = None
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def recurse_tree(current_node):
      # If reached the end of a branch, return False.
      if not current_node:
        return False
      # Left Recursion
      left = recurse_tree(current_node.left)
      # Right Recursion
      right = recurse_tree(current_node.right)
      # If the current node is one of p or q
      mid = current_node == p or current_node == q
      # If any two of the three flags left, right or mid become True.
      if mid + left + right >= 2:
        self.ans = current_node
        raise
      # Return True if either of the three bool values is True.
      return mid or left or right
    # Traverse the tree
    try:
      recurse_tree(root)
    except:
      pass
    return self.ans