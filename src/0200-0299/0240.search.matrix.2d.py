from typing import List

class Solution:
  def recursive(self, il, ir, jl, jr):
    if il > ir or jl > jr:
      return False
    im = (il + ir) // 2
    jm = (jl + jr) // 2
    if self.matrix[im][jm] == self.target:
      return True
    elif self.matrix[im][jm] > self.target:
      if self.recursive(il, im - 1, jl, jm - 1):
        return True
      # hill: off-diagonal blocks
      if self.recursive(il, im - 1, jm, jr):
        return True
      if self.recursive(im, ir, jl, jm - 1):
        return True
    else:
      # self.matrix[im][jm] < self.target
      if self.recursive(im + 1, ir, jm + 1, jr):
        return True
      # hill: off-diagonal blocks
      if self.recursive(im + 1, ir, jl, jm):
        return True
      if self.recursive(il, im, jm + 1, jr):
        return True
    return False
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    """modified binary search, remove 1/4 each iteration, ((3/4)*N)^k = 1, k ~= O(logN), N=n*m.
    """
    n = len(matrix)
    if n == 0:
      return False
    m = len(matrix[0])
    if m == 0:
      return False
    self.matrix = matrix
    self.target = target
    return self.recursive(0, n - 1, 0, m - 1) 

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    """move along the row and col w.r.t sorted property, O(n + m).
    """
    n = len(matrix)
    if n == 0:
      return False
    m = len(matrix[0])
    if m == 0:
      return False
    # kind like middle
    i, j = n - 1, 0
    while i >= 0 and j < m:
      if matrix[i][j] == target:
        return True
      elif matrix[i][j] > target:
        i -= 1
      else:
        j += 1
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5),
    ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20),
    ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 23),
  ]
  rslts = [solver.searchMatrix(matrix, target) for matrix, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")