"""Definition for a QuadTree node.
class Node:
  def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
    self.val = val
    self.isLeaf = isLeaf
    self.topLeft = topLeft
    self.topRight = topRight
    self.bottomLeft = bottomLeft
    self.bottomRight = bottomRight
"""

class Solution:
  def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
    """Q0427
    """
    node = Node(0, 0, None, None, None, None)
    node1, node2 = quadTree1, quadTree2
    if node1 and node2:
      if node1.isLeaf and node2.isLeaf:
        node.isLeaf = 1
        node.val = (node1.val | node2.val)
      elif node1.isLeaf:
        if node1.val == 1:
          node = node1
        else:
          node = node2
      elif node2.isLeaf:
        if node2.val == 1:
          node = node2
        else:
          node = node1
      else:
        node.topLeft = self.intersect(node1.topLeft, node2.topLeft)
        node.topRight = self.intersect(node1.topRight, node2.topRight)
        node.bottomLeft = self.intersect(node1.bottomLeft, node2.bottomLeft)
        node.bottomRight = self.intersect(node1.bottomRight, node2.bottomRight)
        # combine when all quads are leaf with equal value
        allisLeaf = node.topLeft.isLeaf and node.topRight.isLeaf and node.bottomLeft.isLeaf and node.bottomRight.isLeaf
        allEqualVal = node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val
        if allisLeaf and allEqualVal:
          node.isLeaf = 1
          node.val = node.topLeft.val
          node.topLeft = None
          node.topRight = None
          node.bottomLeft = None
          node.bottomRight = None
    elif node1:
      node = node1
    elif node2:
      node = node2
    else:
      node = None
    return node

# Test Cases

# quadTree1 = [[1,0]]
# quadTree2 = [[1,0]]
# output: [[1,0]]

# quadTree1 = [[0,0],[1,0],[1,0],[1,1],[1,1]]
# quadTree2 = [[0,0],[1,1],[1,1],[1,0],[1,1]]
# output: [[1,1]]

# quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]
# quadTree2 = [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# output: [[0,0],[1,1],[1,1],[1,1],[1,0]]