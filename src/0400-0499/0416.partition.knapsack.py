from typing import List

class Solution:
  def canPartition(self, nums: List[int]) -> bool:
    """Knapsack, dynamic programming.
    """
    n = len(nums)
    w = sum(nums)
    if w & 1:
      return False
    w = w // 2
    # dp - up to i-th item, what are the ok sums?
    dp = [[False] * (w + 1) for i in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
      dp[i][0] = True
      for j in range(w + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= nums[i - 1]:
          dp[i][j] |= dp[i - 1][j - nums[i - 1]]
    return dp[n][w]

class Solution:
  def canPartition(self, nums: List[int]) -> bool:
    """set of possible sum <= sum(nums) // 2
    """
    n = len(nums)
    w = sum(nums)
    if w & 1:
      return False
    w = w // 2
    s = set([0])
    for x in nums:
      snext = {x + y for y in s if x + y <= w}
      if w in snext:
        return True
      s |= snext 
    return w in s

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0],
    [1],
    [1,2,3,4],
    [1,2,3,5],
    [23,13,11,7,6,5,5],
  ]
  rslts = [solver.canPartition(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
