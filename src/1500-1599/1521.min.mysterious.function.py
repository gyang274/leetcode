from typing import List

class Solution:
  def closestToTarget(self, nums: List[int], target: int) -> int:
    s, ans = set(), float('inf')
    for x in nums:
      # &() operations is none-increasing in terms of num of bit 1s, so |s| ~O(logM), M = max(nums)
      s = {y & x for y in s} | {x}
      f = {}
      for z in s:
        ans = min(ans, abs(z - target))
        # &() operation is none increasing in terms of value itself..
        if z > target:
          f.add(z)
      s = f
    return ans
