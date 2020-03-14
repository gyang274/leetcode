from typing import List

class Solution:
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    """dynamic programming, O(N^2)
      sort nums, dp[i] = max(dp[j]) + 1, where nums[i] % nums[j] == 0, j < i
    """
    n = len(nums)
    if n == 0:
      return []
    # sort
    nums.sort()
    # dynamic programing + boundary set
    # dp: key by nums, value (1, []) max length of divisible set and what should be go before
    ans, dp = [], [[] for _ in nums]
    for i in range(n):
      for j in range(i):
        if nums[i] % nums[j] == 0:
          if len(dp[i]) - len(dp[j]) <= 0:
            dp[i] = dp[j][:]
      dp[i].append(nums[i])
      if len(dp[i]) > len(ans):
        ans = dp[i]
    return ans

class Solution:
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    S = {-1: set()}
    for x in sorted(nums):
      S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
    return list(max(S.values(), key=len))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [546,669],
    [1,2,3,4,5,6,7,8,9,10],
  ]
  rslts = [solver.largestDivisibleSubset(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")