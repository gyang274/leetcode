"""Definition for a Node.
class Node(object):
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children
"""

from collections import deque

class Codec:
  def serialize(self, root: 'Node') -> str:
    """Encodes a tree to a single string.
    """
    s = []
    if root:
      queue = deque([root, None, ])
      while queue:
        node = queue.popleft()
        if node:
          s.append(str(node.val))
          for nc in node.children:
            queue.append(nc)
          # node-wise and level-wise separation
          queue.append(None)
        else:
          s.append("")
    return ",".join(s)

  def deserialize(self, data: str) -> 'Node':
    """Decodes your encoded data to tree.
    """
    if data == "":
      return None
    d = data.split(",")
    root = Node(int(d[0]), [])
    i, j, q = 0, 2, [root]
    while j < len(d):
      node = q[i]
      i += 1
      while not d[j] == "":
        nc = Node(int(d[j]), [])
        node.children.append(nc)
        q.append(nc)
        j += 1
      j += 1
    return root

# [1,null,3,2,4,null,5,6]
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]