from typing import List

class Solution:
  def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    if m == 0:
      return []
    n = len(matrix[0])
    if n == 0:
      return []
    ans, dd = [], 1
    for d in range(m + n - 1):
      dd ^= 1
      if dd:
        for i in range(max(0, d - n + 1), min(m, d + 1)):
          ans.append(matrix[i][d - i])
      else:
        for i in range(min(m - 1, d), max(-1, d - n), -1):
          ans.append(matrix[i][d - i])
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[2,3]],
    [[1,2,3],[4,5,6],[7,8,9]],
  ]
  rslts = [solver.findDiagonalOrder(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  