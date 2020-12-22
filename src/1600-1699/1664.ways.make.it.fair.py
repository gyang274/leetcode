from typing import List

class Solution:
  def waysToMakeFair(self, nums: List[int]) -> int:
    # lo, le: sum of odds and evens without last item on leftr
    # ro, re: sum of odds and evens without last item on right
    # all indices' odd or even are referring to original index 
    lo, le, ro, re = 0, 0, sum(nums[1::2]), sum(nums[::2])
    i, n, count = 0, len(nums), 0
    while i < n:
      # move nums[i] from right to left as processed
      lo += (i & 1) * nums[i]
      le += ((i & 1) ^ 1) * nums[i]
      ro -= (i & 1) * nums[i]
      re -= ((i & 1) ^ 1) * nums[i]
      if lo + re - (i & 1) * nums[i] == le + ro - ((i & 1) ^ 1) * nums[i]:
        count += 1
      i += 1
    return count
