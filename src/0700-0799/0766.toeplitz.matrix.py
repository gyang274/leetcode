class Solution:
  def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
      for j in range(n):
        if not (i == 0 or j == 0 or matrix[i][j] == matrix[i - 1][j - 1]):
          return False
    return True
