from typing import List

class Solution:
  def minOperations(self, nums: List[int], x: int) -> int:
    # find longest subarray such that sum is sum(nums) - x
    # algo: binary search O(NlogN), or sliding window O(N)
    i, j, n = 0, 0, len(nums)
    # s: sum of current subarray
    # t: target subarray sum to reach
    # r: length of subarray reached target sum
    r, s, t = -1, 0, sum(nums) - x
    # slide window
    while i < n:
      s += nums[i]
      i += 1
      if s < t:
        continue
      elif s > t:
        while s > t and i > j:
          s -= nums[j]
          j += 1
      if s == t:
        r = max(r, i - j)
    return r if r == -1 else n - r
