from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    """dynamic programming: dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    """
    if len(nums) < 2:
      return sum(nums)
    else:
      s1, s2 = nums[0], max(nums[0], nums[1])
      for i in range(2, len(nums)):
        s1, s2 = s2, max(s2, s1 + nums[i])
    return s2

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1],
    [1,1],
    [2,3,2],
    [1,2,3,1],
    [2,7,9,3,1],
    [1,3,1,3,100],
  ]
  rslts = [solver.rob(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}") 