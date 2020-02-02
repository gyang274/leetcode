from typing import List


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
  def __repr__(self):
    s, l, r = str(self.val), str(self.left.val) if self.left else '#', str(self.right.val) if self.right else '#'
    u = len(s)
    n, p, x = len(l), 1, len(l) // 2
    m, q, y = len(r), 1, len(r) // 2
    ln0 = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    ln1 = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
      l += [n * ' '] * (q - p)
    elif q < p:
      r += [m * ' '] * (q - p)
    ln2 = l + u * ' ' + r
    return '\n'.join([ln0, ln1, ln2])
  # display the entire subtree rooted at this node
  def display(self):
    lines, _, _, _ = self._display_aux()
    return '\n'.join(lines)
  def _display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root.
    """
    # No child.
    if self.right is None and self.left is None:
      line = '%s' % self.val
      width = len(line)
      height = 1
      middle = width // 2
      return [line], width, height, middle
    # Only left child.
    if self.right is None:
      lines, n, p, x = self.left._display_aux()
      s = '%s' % self.val
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
      second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
      shifted_lines = [line + u * ' ' for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
    # Only right child.
    if self.left is None:
      lines, n, p, x = self.right._display_aux()
      s = '%s' % self.val
      u = len(s)
      first_line = s + x * '_' + (n - x) * ' '
      second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
      shifted_lines = [u * ' ' + line for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
    # Two children.
    left, n, p, x = self.left._display_aux()
    right, m, q, y = self.right._display_aux()
    s = '%s' % self.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
      left += [n * ' '] * (q - p)
    elif q < p:
      right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


def listToTreeNode(x: List) -> TreeNode:
  if not x:
    return None
  root = TreeNode(x[0])
  i, j, q = 0, 1, [root]
  while j < len(x):
    node = q[i]
    i += 1
    item = x[j]
    j += 1
    if item is not None:
      node.left = TreeNode(item)
      q.append(node.left)
    if j < len(x):
      item = x[j]
      j += 1
      if item is not None:
        node.right = TreeNode(item)
        q.append(node.right)
  return root


# inorder: (left, root/self, right)
def inorderTraversal(root: TreeNode, method: str = 'it') -> List:
  """inorder traversal of a binary tree.
  """
  if method == 'it':
    return inorderTraversalIterative(root)
  elif method == 're':
    return inorderTraversalRecursive(root)
  elif method == 'mr':
    return inorderTraversalMorrisive(root)
  else:
    return NotImplementedError

def inorderTraversalIterative(root: TreeNode) -> List:
  """Iterative.
  """
  x = []
  if root is not None:
    node, stack = root, []
    while node or stack:
      while node:
        stack.append(node)
        node = node.left
      node = stack.pop()
      x.append(node.val)
      node = node.right
  return x

def inorderTraversalRecursive(root: TreeNode) -> List:
  """Recursive.
  """
  def recursive(x, root):
    if root.left is not None:
      recursive(x, root.left)
    x.append(root.val)
    if root.right is not None:
      recursive(x, root.right)
  x = []
  if root is not None:
    recursive(x, root)
  return x

def inorderTraversalMorrisive(root: TreeNode) -> List:
  """Morris Traversal.
  """
  x = []
  if root is not None:
    node = root
    while node:
      if not node.left:
        x.append(node.val)
        node = node.right
      else:
        prev = node.left
        while prev.right:
          prev = prev.right
        prev.right = node
        # hold = node
        # node = node.left
        # hold.left = None
        # note: node, node.left =  node.left , None; will cause loop, wrong!
        node.left, node = None, node.left 
  return x


def inorderTreeNodeToList(root: TreeNode) -> List:
  """inorder representation of tree as list with none.
  """
  return NotImplemented


def inorderListToTreeNode(x: List) -> TreeNode:
  """inorder representation of tree as list with none back to root (TreeNode).
  """
  return NotImplemented


# preorder: (root/self, left, right)
def preorderTraversal(root: TreeNode, method: str = 'it') -> List:
  """preorder traversal of a binary tree.
  """
  if method == 'it':
    return preorderTraversalIterative(root)
  elif method == 're':
    return preorderTraversalRecursive(root)
  elif method == 'mr':
    return preorderTraversalMorrisive(root)
  else:
    return NotImplementedError

def preorderTraversalIterative(root: TreeNode) -> List:
  """Iterative.
  """
  x = []
  if root is not None:
    stack = [root, ]
    while stack:
      node = stack.pop()
      if node is not None:
        x.append(node.val)
        if node.right is not None:
          stack.append(node.right)
        if node.left is not None:
          stack.append(node.left)
  return x

def preorderTraversalRecursive(root: TreeNode) -> List:
  """Recursive.
  """
  def recursive(x, root):
    x.append(root.val)
    if root.left is not None:
      recursive(x, root.left)
    if root.right is not None:
      recursive(x, root.right)
  x = []
  if root is not None:
    recursive(x, root)
  return x

def preorderTraversalMorrisive(root: TreeNode) -> List:
  """Morris Traversal.
  """
  node, x = root, []
  while node is not None:
    if node.left is None:
      x.append(node.val)
      node = node.right
    else:
      prev = node.left
      while prev.right is not None and prev.right is not node:
        prev = prev.right
      if prev.right is None:
        x.append(node.val)
        prev.right = node
        node = node.left
      else:
        prev.right = None
        node = node.right
  return x


def preorderTreeNodeToList(root: TreeNode) -> List:
  """preorder representation of tree as list with none.
  """
  x = []
  if root is not None:
    stack = [root, ]
    while stack:
      node = stack.pop()
      if node is not None:
        x.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
      else:
        x.append(None)
  return x


def preorderListToTreeNode(x: List) -> TreeNode:
  """preorder representation of tree as list with none back to root (TreeNode).
  """
  if not x:
    return None
  root = TreeNode(x[0])
  i, stack = 1, [root, ]
  while i < len(x):
    item, node = x[i], stack[-1]
    if node.left is None and x[i - 1] is not None:
      if item is not None:
        node.left = TreeNode(item)
        stack.append(node.left)
    else:
      stack.pop()
      if item is not None:
        node.right = TreeNode(item)
        stack.append(node.right)
    i += 1
  return root


# postorder: (left, right, root/self)
def postorderTraversal(root: TreeNode, method: str = 'it') -> List:
  """postorder traversal of a binary tree.
  """
  if method == 'it':
    return postorderTraversalIterative(root)
  elif method == 're':
    return postorderTraversalRecursive(root)
  else:
    return NotImplementedError

def postorderTraversalIterative(root: TreeNode) -> List:
  """Iterative.
  """
  x = []
  if root is not None:
    stack = [root, ]
    while stack:
      node = stack.pop()
      x.append(node.val)
      if node.left is not None:
        stack.append(node.left)
      if node.right is not None:
        stack.append(node.right)
  return list(reversed(x))

def postorderTraversalRecursive(root: TreeNode) -> List:
  """Recursive.
  """
  def recursive(x, root):
    if root.left is not None:
      recursive(x, root.left)
    if root.right is not None:
      recursive(x, root.right)
    x.append(root.val)
  x = []
  if root is not None:
    recursive(x, root)
  return x


def postorderTreeNodeToList(root: TreeNode) -> List:
  """postorder representation of tree as list with none.
  """
  return NotImplemented


def postorderListToTreeNode(x: List) -> TreeNode:
  """postorder representation of tree as list with none back to root (TreeNode).
  """
  return NotImplemented


if __name__ == '__main__':
  # treenode
  print('treenode')
  r = TreeNode(0)
  print(r)
  r.left = TreeNode(1)
  print(r)
  r.right = TreeNode(2)
  print(r)
  r.left.left = TreeNode(3)
  r.left.right = TreeNode(4)
  r.left.right.left = TreeNode(5)
  print(r)
  print(r.display())
  # list to treenode
  r = listToTreeNode([1, 3, 4, 2, None, 5, None, 7, 8, 6, 9, 0, None, None, 2])
  print(r.display())
  # inorder traversal
  print('inorder traversal')
  x = inorderTraversal(r, method='it')
  print(x)
  x = inorderTraversal(r, method='re')
  print(x)
  x = inorderTraversal(r, method='mr')
  print(x)
  # preorder traversal
  print('preorder traversal')
  x = preorderTraversal(r, method='it')
  print(x)
  x = preorderTraversal(r, method='re')
  print(x)
  x = preorderTraversal(r, method='mr')
  print(x)
  print('preorder traversal with none, reconstruction')
  x = preorderTreeNodeToList(r)
  print(x)
  r = preorderListToTreeNode(x)
  print(r.display())
  # postorder traversal
  print('postorder traversal')
  x = preorderTraversal(r, method='it')
  print(x)
  x = preorderTraversal(r, method='re')
  print(x)