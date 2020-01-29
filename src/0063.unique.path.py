from typing import List


class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    obstacle = 0
    for i in range(m):
      if obstacleGrid[i][0] == 1:
        obstacle = 1
      if obstacle == 0:
        dp[i][0] = 1
      else:
        dp[i][0] = 0
    obstacle = 0
    for j in range(n):
      if obstacleGrid[0][j] == 1:
        obstacle = 1
      if obstacle == 0:
        dp[0][j] = 1
      else:
        dp[0][j] = 0
    for i in range(1, m):
      for j in range(1, n):
        if obstacleGrid[i][j] == 1:
          dp[i][j] = 0
        else:
          dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m - 1][n - 1]


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ],
    [
      [0,0,0,0,0,0],
      [0,1,0,0,1,0],
      [0,0,0,0,0,0]
    ]
  ]
  rslts = [solver.uniquePathsWithObstacles(obstacleGrid) for obstacleGrid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")