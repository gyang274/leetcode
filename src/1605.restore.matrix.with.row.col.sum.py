from typing import List

class Solution:
  def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    m, n = len(rowSum), len(colSum)
    x = [[0] * n for _ in range(m)]
    for i in range(m):
      for j in range(n):
        x[i][j] = min(rowSum[i], colSum[j])
        rowSum[i] -= x[i][j]
        colSum[j] -= x[i][j]
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([0], [0]),
    ([0,1], [1]),
    ([3,8], [4,7]),
    ([14,9], [6,9,8]),
    ([5,7,10], [8,6,8]),
  ]
  rslts = [solver.restoreMatrix(rowSum, colSum) for rowSum, colSum in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
