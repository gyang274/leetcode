from typing import List

import math

class Solution:
  def recursive(self, nums):
    n = len(nums)
    if n < 3:
      return 1
    r = nums[0]
    rl = [x for x in nums if x < r]
    rr = [x for x in nums if x > r]
    return math.comb(n - 1, len(rl)) * self.recursive(rl) * self.recursive(rr)
  def numOfWays(self, nums: List[int]) -> int:
    return (self.recursive(nums) - 1) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.numOfWays(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
