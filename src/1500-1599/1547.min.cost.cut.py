from typing import List
from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, n, cuts):
    if len(cuts) == 0:
      return 0
    if len(cuts) == 1:
      return n
    cost = float('inf')
    for i, x in enumerate(cuts):
      cost = min(cost, n + self.recursive(x, cuts[:i]) + self.recursive(n - x, tuple(y - x for y in cuts[(i + 1):])))
    return cost
  def minCost(self, n: int, cuts: List[int]) -> int:
    return self.recursive(n, tuple(sorted(cuts)))

class Solution:
  def minCost(self, n: int, cuts: List[int]) -> int:
    # dynamic programming
    # TC: O(N^3), SC: O(N^2) or O(N) if optimized, 
    # bridge by distance, refr. Q1000, Floyd–Warshall algorithm, ..
    K = sorted(cuts + [0, n])
    m = len(K)
    dp = [[0] * m for _ in range(m)]
    for d in range(2, m):
      for i in range(m - d):
        dp[i][i + d] = (K[i + d] - K[i]) + min(dp[i][j] + dp[j][i + d] for j in range(i + 1, i + d))
    return dp[0][m - 1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (14, [2,3,5,8]),
  ]
  rslts = [solver.minCost(n, cuts) for n, cuts in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
