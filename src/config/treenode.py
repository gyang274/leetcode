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


def inOrderTraversal(root):
  return None


def preOrderTraversal(root):
  return None


def postOrderTraversal(root):
  return None


if __name__ == '__main__':
  # treenode
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