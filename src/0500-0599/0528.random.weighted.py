import random

class Solution:
  def __init__(self, w: List[int]):
    # prefix sum and binary search  
    self.n = sum(w)
    # self.w: prefix sum as threshold of index i
    self.w = w
    for i in range(1, len(w)):
      self.w[i] += self.w[i - 1]

  def pickIndex(self) -> int:
    x = random.randrange(self.n)
    # binary search over prefix sum
    l, r = 0, len(self.w)
    while l < r:
      m = l + (r - l) // 2
      if self.w[m] > x:
        r = m
      else:
        l = m + 1
    return l