from typing import List

class Solution:
  def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
    m, n = len(A), len(B)
    # dynamic programming
    # dp[i][j]: max uncrossed lines with A[:i] and B[:j]
    # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (A[i - 1] == B[j - 1]))
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (A[i - 1] == B[j - 1]))
    return dp[m][n]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,4,2], [1,2,4]),
    ([1,4,2,1], [1,2,4,2]),
    ([2,5,1,2,5], [8,5,2,1,5,2]),
    ([1,3,7,1,7,5], [1,9,2,5,1]),
  ]
  rslts = [solver.maxUncrossedLines(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
