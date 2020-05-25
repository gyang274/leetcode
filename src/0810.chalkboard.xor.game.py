from typing import List
from collections import Counter
from functools import reduce

class Solution:
  def recursive(self, d, x):
    if not sum(d.values()) or not x:
      return True
    for k in d:
      if d[k] > 0:
        d[k] -= 1
        if not self.recursive(d, x ^ k):
          return True
        d[k] += 1
    return False
  def xorGame(self, nums: List[int]) -> bool:
    d = Counter(nums)
    x = reduce((lambda x, y: x ^ y), nums)
    return self.recursive(d, x)

import operator

class Solution:
  def xorGame(self, nums: List[int]) -> bool:
    return len(nums) % 2 == 0 or reduce(operator.xor, nums) == 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1],
    [1,1],
    [1,1,1],
    [1,1,2],
    [1,1,1,2],
  ]
  rslts = [solver.xorGame(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
