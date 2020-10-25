from typing import List
from functools import lru_cache

import itertools

class Solution:
  @lru_cache(None)
  def recursive(self, i, j):
    if i == self.m:
      return 0
    p, ans = 0, self.recursive(i + 1, j)
    for k in range(j, self.n):
      q = self.nums1[i] * self.nums2[k]
      if q > p:
        p = q
        ans = max(ans, p + self.recursive(i + 1, k + 1))
    return ans
  def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    # corner case
    if (
      all(map(lambda x: x <= 0, nums1)) and all(map(lambda x: x >= 0, nums2))
    ) or (
      all(map(lambda x: x >= 0, nums1)) and all(map(lambda x: x <= 0, nums2))
    ):
      return max(x * y for x, y in itertools.product(nums1, nums2))
    # dp
    self.m, self.n = len(nums1), len(nums2)
    self.nums1, self.nums2 = nums1, nums2
    self.recursive.cache_clear()
    return self.recursive(0, 0)

class Solution:
  def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    # TC: O(MN), SC: O(MN), refr. longest common sequence, Q1035
    m, n = len(nums1), len(nums2)
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
      for j in range(n):
        dp[i][j] = nums1[i] * nums2[j]
        if i and j:
          dp[i][j] += max(dp[i - 1][j - 1], 0)
        if i:
          dp[i][j] = max(dp[i][j], dp[i - 1][j])
        if j:
          dp[i][j] = max(dp[i][j], dp[i][j - 1])
    return dp[m - 1][n - 1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([3,-2], [2,-6,7]),
    ([-5,-1,-2], [3,3,5,5]),
    ([2,3,-1,1,-4], [3,2,1,0,4]),
  ]
  rslts = [solver.maxDotProduct(nums1, nums2) for nums1, nums2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
