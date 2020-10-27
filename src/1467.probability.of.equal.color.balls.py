from typing import List
from math import comb, prod
from itertools import accumulate

class Solution:
  def getCombinations(self, balls, l, r, d):
    # l, r: number of available position on left and right,
    # d: difference of number of distinct color on left and right.
    if not balls:
      return d == 0
    if abs(d) > len(balls):
      return 0
    x, count = balls.pop(), 0
    for i in range(x + 1):
      if l >= i and r >= x - i:
        count += comb(l, i) * comb(r, x - i) * self.getCombinations(
          balls.copy(), l - i, r - (x - i), d - (i == 0) + (i == x)
        )
    return count
  def getProbability(self, balls: List[int]) -> float:
    n = sum(balls)
    total = prod(comb(n, x) for n, x in zip(accumulate(balls), balls))
    count = self.getCombinations(balls, n // 2, n // 2, 0)
    return count / total

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,1],
    [1,1,2],
    [1,2,3],
    [1,2,1,2],
    [1,2,4,1,2],
    [6,6,6,6,6,6],
  ]
  rslts = [solver.getProbability(balls) for balls in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
