from typing import List

import heapq

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    nums = [-x for x in nums]
    heapq.heapify(nums)
    return (heapq.heappop(nums) + 1) * (heapq.heappop(nums) + 1)
