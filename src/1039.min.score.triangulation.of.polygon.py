from typing import List, Tuple
from functools import lru_cache, reduce

import operator

class Solution:
  @lru_cache(None)
  def recursive(self, A: Tuple[int]) -> int:
    # dynamic programming
    n = len(A)
    if n == 3:
      return reduce(operator.mul, A)
    return min(A[i - 1] * A[i] * A[(i + 1) % n] + self.minScoreTriangulation(A[:i] + A[(i + 1):]) for i in range(n))
  def minScoreTriangulation(self, A: List[int]) -> int:
    return self.recursive(tuple(A))

class Solution:
  def minScoreTriangulation(self, A: List[int]) -> int:
    # dynamic programming
    # dp[i][k]: triangulate A[i] ~ A[k], O(N^3)
    n = len(A)
    dp = [[0] * n for _ in range(n)]
    # note the sequence, must triangulate polygon3, then polygon4, then polygon5, and etc.
    for d in range(2, n):
      for i in range(n - d):
        k = i + d
        dp[i][k] = min(dp[i][j] + dp[j][k] + A[i] * A[j] * A[k] for j in range(i + 1, k))
    return dp[0][n - 1]

class Solution:
  def minScoreTriangulation(self, A: List[int]) -> int:
    memo = {}
    def dp(i, k):
      if (i, k) not in memo:
        memo[(i, k)] = min([dp(i, j) + dp(j, k) + A[i] * A[j] * A[k] for j in range(i + 1, k)] or [0])
      return memo[(i, k)]
    return dp(0, len(A) - 1)


if __name__ == '__main__':
  solver = Solution()
  cases = [
    # [1,2,3],
    # [2,7,4,5],
    # [1,3,1,4,1,5],
    [35,73,90,27,71,80,21,33,33,13,48,12,68,70,80,36,66,3,70,58],
  ]
  rslts = [solver.minScoreTriangulation(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
