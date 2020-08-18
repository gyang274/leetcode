from typing import List
from functools import lru_cache
from itertools import accumulate

class Solution:
  @lru_cache(None)
  def recursive(self, i, m):
    # return the max difference of current player stone - opponent player stone
    if i + 2 * m >= self.n:
      return self.piles[self.n] - self.piles[i]
    d = float('-inf')
    for x in range(1, 2 * m + 1):
      d = max(d, (self.piles[i + x] - self.piles[i]) - self.recursive(i + x, max(m, x)))
    return d
  def stoneGameII(self, piles: List[int]) -> int:
    self.recursive.cache_clear()
    self.piles, self.n = list(accumulate(piles, initial = 0)), len(piles)
    return (self.piles[self.n] + self.recursive(0, 1)) // 2

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [2,7,9,4,4],
  ]
  rslts = [solver.stoneGameII(piles) for piles in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
