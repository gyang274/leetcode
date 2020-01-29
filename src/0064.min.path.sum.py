from typing import List


class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dp = grid.copy()
    for i in range(1, m):
      dp[i][0] = dp[i - 1][0] + dp[i][0]
    for j in range(1, n):
      dp[0][j] = dp[0][j - 1] + dp[0][j]
    for i in range(1, m):
      for j in range(1, n):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]
    return dp[m - 1][n - 1]


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ],
    [
      [1,3,2,3,1],
      [1,5,4,2,1],
      [1,2,3,5,1]
    ],
  ]
  rslts = [solver.minPathSum(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
