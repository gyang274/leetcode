from typing import List

import heapq

class Solution:
  def minimumDeviation(self, nums: List[int]) -> int:
    # priority queue, TC: O(NlogN), SC: O(N)
    n = len(nums)
    # odd can double only once, even cannot double, double all odds to queue -> all even, all can divide by 2 any times.
    q = [-x * 2 if x & 1 else -x for x in nums]
    heapq.heapify(q)
    # l: min value on hold
    l, d = -max(q), float('-inf')
    while len(q) == n:
      x = -heapq.heappop(q)
      d = min(d, x - l)
      if (x & 1) ^ 1:
        l = min(l, x // 2)
        heapq.heappush(q, -x // 2)
    return d
