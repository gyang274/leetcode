from typing import List

class Solution:
  def recursive(self, target):
    if target not in self.memo:
      self.memo[target] = 0
      if target >= self.nums[0]:  
        for x in self.nums:
          if target - x >= 0:
            self.memo[target] += self.recursive(target - x)
    return self.memo[target]
  def combinationSum4(self, nums: List[int], target: int) -> int:
    """Q0039.
    """
    if target <= 0:
      return 0
    if len(nums) == 0:
      return 0
    self.nums = nums
    self.nums.sort()
    # key by target
    self.memo = {0: 1}
    # recursive + memo
    return self.recursive(target)

class Solution(object):
  def combinationSum4(self, nums: List[int], target: int) -> int:
    """Q0039, dynamic programming.
    """
    if target <= 0:
      return 0
    if len(nums) == 0:
      return 0
    nums.sort()
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(target + 1):
      for x in nums:
        if x <= i:
          dp[i] += dp[i - x]
    return dp[target]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([], 1),
    ([1], 4),
    ([2], 3),
    ([1,2,3], 4),
    ([1,2,3,5,8], 42)
  ]
  rslts = [solver.combinationSum4(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  