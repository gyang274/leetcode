from typing import List
from collections import Counter

class Solution:
  def maximumUniqueSubarray(self, nums: List[int]) -> int:
    d, i, j, n, m, x, = Counter(), 0, 0, len(nums), 0, 0
    while j < n:
      d[nums[j]] += 1
      x += nums[j]
      while d[nums[j]] > 1:
        d[nums[i]] -= 1
        x -= nums[i]
        i += 1
      m = max(m, x)
      j += 1
    return m