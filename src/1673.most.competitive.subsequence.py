from typing import List

class Solution:
  def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
    # stack, TC: O(N), SC: O(1)
    s, n = [], len(nums)
    for i, x in enumerate(nums):
      while s and len(s) + (n - i) > k and x < s[-1]:
        s.pop()
      if len(s) < k:
        s.append(x)
    return s
