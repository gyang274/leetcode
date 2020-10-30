# Definition for Node.
# class Node:
#   def __init__(self, val=0, left=None, right=None, random=None):
#     self.val = val
#     self.left = left
#     self.right = right
#     self.random = random

class Solution:
  def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
    # two pass, 1st pass create node, 2nd pass create link
    queue, qcopy = [root], []
    # 1st pass
    for node in queue:
      if node:
        # create deep copy
        qcopy.append(NodeCopy(node.val))
        # append to the list
        queue.append(node.left)
        queue.append(node.right)
      else:
        qcopy.append(None)
    # 2nd pass
    # node to index
    d = {node: i for i, node in enumerate(queue) if node}
    for i, node in enumerate(queue):
      if node:
        if node.left:
          qcopy[i].left = qcopy[d[node.left]]
        if node.right:
          qcopy[i].right = qcopy[d[node.right]]
        if node.random:
          qcopy[i].random = qcopy[d[node.random]]
    return qcopy[0]
