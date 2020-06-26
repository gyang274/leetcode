from typing import List
from collections import Counter

class Solution:
  def _getGCD(self, x, y):
    while y:
      x, y = y, x % y
    return x
  # def _getLCM(self, x, y):
  #   return x * y // self._getGCD(x, y)
  def hasGroupsSizeX(self, deck: List[int]) -> bool:
    v = list(Counter(deck).values())
    d = v[0]
    for x in v[1:]:
      d = self._getGCD(d, x)
    return d > 1

from math import gcd
from functools import reduce

class Solution:
  def hasGroupsSizeX(self, deck: List[int]) -> bool:    
    return reduce(gcd, Counter(deck).values()) >= 2

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1],
    [1,1],
    [1,1,2,2],
    [1,1,2,2,2],
  ]
  rslts = [solver.hasGroupsSizeX(deck) for deck in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
