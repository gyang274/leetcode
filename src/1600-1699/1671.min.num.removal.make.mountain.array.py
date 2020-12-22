from typing import List

import bisect

class Solution:
  def minimumMountainRemovals(self, nums: List[int]) -> int:
    # TC: O(NlogN), SC: O(N)
    # min removal is equivalent to find longest mountain array
    n = len(nums)
    # straight increasing from left
    # keep a sorted list of lowest mountain height for a given length of mountain
    L, h = [0] * n, [nums[0]]
    for i in range(1, n):
      k = bisect.bisect_left(h, nums[i])
      L[i] = k
      if k == len(h):
        h.append(nums[i])
      else:
        h[k] = min(h[k], nums[i])
    # straight increasing from right
    # keep a sorted list of lowest mountain height for a given length of mountain
    R, h = [0] * n, [nums[n - 1]]
    for j in range(n - 2, -1, -1):
      k = bisect.bisect_left(h, nums[j])
      R[j] = k
      if k == len(h):
        h.append(nums[j])
      else:
        h[k] = min(h[k], nums[j])
    return n - max(x + y + 1 for x, y in zip(L, R) if x > 0 and y > 0)
