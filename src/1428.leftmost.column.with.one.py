# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix:
#   def get(self, row: int, col: int) -> int:
#   def dimensions(self) -> list[]:

class Solution:
  def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    # TC: O(MlogN), SC: O(1)
    m, n = binaryMatrix.dimensions()
    # binary search to identify 1st one in row[i], say row[i][j]
    # start the search of next row within (0, j) instead of (0, n)
    def search(i, j):
      l, r = 0, j
      while l < r:
        m = l + (r - l) // 2
        if binaryMatrix.get(i, m):
          r = m
        else:
          l = m + 1
      return r
    j = n
    for i in range(m):
      j = search(i, j)
      if j == 0:
        return 0
    return -1 if j == n else j

class Solution:
  def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    # TC: O(M + N), SC: O(1)
    # start from top-right, move only to left-bottom
    rows, cols = binaryMatrix.dimensions()
    # set pointers to the top-right corner.
    current_row, current_col = 0, cols - 1    
    # repeat the search until it goes off the grid.
    while current_row < rows and current_col >= 0:
      if binaryMatrix.get(current_row, current_col) == 0:
        current_row += 1
      else:
        current_col -= 1  
    # if we never left the last column, it must have been all 0's.
    return current_col + 1 if current_col != cols - 1 else -1
