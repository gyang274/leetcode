from typing import List

class Solution:
  def minFallingPathSum(self, A: List[List[int]]) -> int:
    n = len(A)
    # dynamic programming
    # dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i+1][j]) + A[i][j]
    dp = [[None] * n for _ in range(n)]
    dp[0][:] = A[0][:]
    for i in range(1, n):
      dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + A[i][0]
      for j in range(1, n - 1):
        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + A[i][j]
      dp[i][n - 1] = min(dp[i - 1][n - 2], dp[i - 1][n - 1]) + A[i][n - 1]
    return min(dp[n - 1])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2,3],[4,5,6],[7,8,9]],
  ]
  rslts = [solver.minFallingPathSum(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
