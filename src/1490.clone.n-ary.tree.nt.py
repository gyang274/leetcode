"""
# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children if children is not None else []
"""

class Solution:
  def cloneTree(self, root: 'Node') -> 'Node':
    # Q0133, bfs, dfs
    if not root:
      return None
    # clone the root
    rcopy = Node(root.val)
    # clone: all nodes has been cloned.
    # stack: stack of unvisited clones.
    clone, stack = {root: rcopy}, set([(root, rcopy), ])
    while stack:
      node, copy = stack.pop()
      for nx in node.children:
        if nx not in clone:
          nc = Node(nx.val)
          clone[nx] = nc
          stack.add((nx, nc))
        copy.children.append(nc)
    return rcopy
