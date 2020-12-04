from typing import List
from collections import Counter, defaultdict
from functools import lru_cache

class Solution:
  def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
    # dp + bitmask, O(50*(3^m))
    # d: counts of each unique value
    d = sorted(Counter(nums).values(), reverse=True)
    # n: num of unique values in nums, the exact value itself doesn't matter
    n, m = len(d), len(quantity)
    # q: sum of quantities required by such mask ones
    q = defaultdict(int)
    for mask in range(1 << m):
      for i in range(m):
        if (1 << i) & mask:
          q[mask] += quantity[i]
    # dp
    @lru_cache(None)
    def recursive(i, mask):
      if mask == 0:
        return True
      if i == n:
        return False
      # iterate over all submask
      submask = mask
      while submask:
        if q[submask] <= d[i] and recursive(i + 1, mask ^ submask):
          return True
        submask = (submask - 1) & mask
      # return recursive(i + 1, mask)
      # d is sorted reversely, so no need to recursive next when no reduction..
      return False
    # satisify all when all available
    return recursive(0, (1 << m) - 1)
