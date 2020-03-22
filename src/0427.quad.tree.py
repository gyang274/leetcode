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

class NumMatrix:
  def __init__(self, matrix: List[List[int]]):
    """store partial sum of 0-i, 0-j for i<n, j<m so any range sum is O(1).
    """
    n = len(matrix)
    if n > 0:
      m = len(matrix[0])
      if m > 0:
        for i in range(1, n):
          matrix[i][0] += matrix[i - 1][0]
        for j in range(1, m):
          matrix[0][j] += matrix[0][j - 1]
        for i in range(1, n):
          for j in range(1, m):
            matrix[i][j] += matrix[i][j - 1] + matrix[i - 1][j] - matrix[i - 1][j - 1]
    self.matrix = matrix
  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    x = self.matrix[row2][col2] 
    x -= self.matrix[row1 - 1][col2] if row1 > 0 else 0
    x -= self.matrix[row2][col1 - 1] if col1 > 0 else 0
    x += self.matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
    return x

class Solution:
  def recursive(self, row1, col1, row2, col2):
    # sum of region in O(1)
    sr = self.nums.sumRegion(row1, col1, row2, col2)
    # init node
    node = Node(0, 0, None, None, None, None)
    # isLeaf
    if sr == 0 or sr == (row2 - row1 + 1) * (col2 - col1 + 1):
      node.isLeaf = 1
      node.val = 0 if sr == 0 else 1
    else:
      node.topLeft = self.recursive(row1, col1, row1 + (row2 - row1) // 2, col1 + (col2 - col1) // 2)
      node.topRight = self.recursive(row1, col1 + (col2 - col1) // 2 + 1, row1 + (row2 - row1) // 2, col2)
      node.bottomLeft = self.recursive(row1 + (row2 - row1) // 2 + 1, col1, row2, col1 + (col2 - col1) // 2)
      node.bottomRight = self.recursive(row1 + (row2 - row1) // 2 + 1, col1 + (col2 - col1) // 2 + 1, row2, col2)
    return node
  def construct(self, grid: List[List[int]]) -> 'Node':
    """Q0304: range sum 2d.
    """
    self.nums = NumMatrix(grid)
    x = self.recursive(0, 0, len(grid) - 1, len(grid) - 1)
    return x
