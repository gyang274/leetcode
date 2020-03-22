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