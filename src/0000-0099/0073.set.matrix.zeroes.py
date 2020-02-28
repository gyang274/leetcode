from typing import List


class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    """Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    # special indicator for 1st row and 1st column 
    fr, fc = 1, 1
    # loop through matrix, use 1st col and 1st row to indicate set 0 or not
    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 0:
          if i == 0:
            fr = 0
          else:
            matrix[i][0] = 0
          if j == 0:
            fc = 0
          else:
            matrix[0][j] = 0
    # set rows w.r.t 1st col
    for i in range(1, m):
      if matrix[i][0] == 0:
        for j in range(1, n):
          matrix[i][j] = 0
    # set cols w.r.t 1st row
    for j in range(1, n):
      if matrix[0][j] == 0:
        for i in range(1, m):
          matrix[i][j] = 0
    # set 1st row
    if fr == 0:
      for j in range(n):
        matrix[0][j] = 0
    # set 1st col
    if fc == 0:
      for i in range(m):
        matrix[i][0] = 0
    return None


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [
      [1,0],
      [1,1],
      [1,2],
    ],
    [
      [1,1,1],
      [0,1,2]
    ],
    # [
    #   [1,1,1],
    #   [1,0,1],
    #   [1,1,1]
    # ],
    # [
    #   [0,1,2,0],
    #   [3,4,5,2],
    #   [1,3,1,5]
    # ],
  ]
  rslts = [solver.setZeroes(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")