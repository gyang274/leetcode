"""Definition for a Node.
class Node: 
  def __init__(self, val = 0, neighbors = []): 
    self.val = val
    self.neighbors = neighbors
"""
class Solution:
  def cloneGraph(self, node: 'Node') -> 'Node':
    """BFS or DFS.
    """
    if node is None: 
      return None 
    # clone from the node
    root = clone = Node(node.val)
    # all nodes had cloned, stack of unvistied cloned nodes (BFS: FIFO stack, DFS: LIFO stack)
    clones, stack = {node: clone}, set([(clone, node), ])
    while stack:
      clone, node = stack.pop()
      for x in node.neighbors:
        if x not in clones:
          xc = Node(x.val)
          clones[x] = xc
          stack.add((xc, x))
        clone.neighbors.append(clones[x])
    return root
