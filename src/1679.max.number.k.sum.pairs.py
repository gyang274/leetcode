from collections import Counter

class Solution:
  def maxOperations(self, nums: List[int], k: int) -> int:
    d, s = Counter(nums), 0
    for x in d:
      if x < (k + 1) // 2:
        s += min(d[x], d[k - x])
    if (k & 1) ^ 1:
      s += d[k // 2] // 2
    return s
