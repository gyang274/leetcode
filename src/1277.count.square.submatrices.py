from typing import List

class Solution:
  def countSquares(self, matrix: List[List[int]]) -> int:
    # TC: O(MN), SC: O(1).
    m, n, count = len(matrix), len(matrix[0]), 0
    # dp:
    # dp[i][j] means the size of biggest square with A[i][j] as bottom-right corner.
    # dp[i][j] also means the number of squares with A[i][j] as bottom-right corner.
    # 
    # if A[i][j] == 0, no possible square.
    # if A[i][j] == 1, compare the size of square dp[i-1][j-1], dp[i-1][j] and dp[i][j-1],
    #   dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 is the maximum size of square that can be found.
    for i in range(1, m):
      for j in range(1, n):
        matrix[i][j] *= min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
    return sum(map(sum, matrix))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,0,1],[1,1,0],[1,1,0]],
    [[0,1,1,1],[1,1,1,1],[0,1,1,1]],
  ]
  rslts = [solver.countSquares(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
