from typing import List


class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    if m == 0:
      return False
    n = len(matrix[0])
    # matrix cell values are sorted according z index
    z = lambda i, j: i * n + j
    zij = lambda z: (z // n, z % n)
    # make binary search w.r.t z
    zl, zr = 0, z(m - 1, n - 1)
    while zl <= zr:
      zm = (zl + zr) // 2
      i, j = zij(zm)
      if matrix[i][j] == target:
        return True
      elif matrix[i][j] < target:
        zl = zm + 1
      else:
        zr = zm - 1 
    return False


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([], 0),
    ([
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ], 3),
    ([
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ], 13)
  ]
  rslts = [solver.searchMatrix(matrix, target) for matrix, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")