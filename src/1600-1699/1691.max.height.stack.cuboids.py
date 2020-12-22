from typing import List

class Solution:
  def maxHeight(self, cuboids: List[List[int]]) -> int:
    # TC: O(N^2 + NlogN), sort + dynamic programming
    n = len(cuboids)
    # cuboid A dominant cuboid B iff aj >= bj for all j = 1,2,3 dimensions
    # x = [[0, 0, 0]] + sorted([sorted(cuboid) for cuboid in cuboids])
    x = [[0, 0, 0]] + sorted(map(sorted, cuboids))
    # dp
    dp = [0] * (n + 1)
    # stack cuboid i on j, when possible, i < j 
    for j in range(1, n + 1):
      for i in range(j):
        if all(x[i][k] <= x[j][k] for k in range(3)):
          dp[j] = max(dp[j], dp[i] + x[j][2])
    return max(dp)
