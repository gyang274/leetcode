class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
      dp[i][0] = 1
    for j in range(n):
      dp[0][j] = 1
    for i in range(1, m):
      for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    (3, 2),
    (5, 4)
  ]
  rslts = [
    solver.uniquePaths(m, n) for (m, n) in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")