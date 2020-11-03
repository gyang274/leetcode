from typing import List
from functools import lru_cache

class Solution:
  @lru_cache(None)
  def _build(self, i, j):
    # build one mailbox for houses[i:(j + 1)]
    d = 0
    while i < j:
      d += self.x[j] - self.x[i]
      i += 1
      j -= 1
    return d
  @lru_cache(None)
  def recursive(self, i, k):
    if k == self.n - i:
      return 0
    if k == 1:
      return self._build(i, self.n - 1)
    ans = float('inf')
    for j in range(i, self.n - k + 1):
      ans = min(ans, self._build(i, j) + self.recursive(j + 1, k - 1))
    return ans
  def minDistance(self, houses: List[int], k: int) -> int:
    self.n, self.x = len(houses), sorted(houses)
    self._build.cache_clear()
    self.recursive.cache_clear()
    return self.recursive(0, k)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([7,4,6,1], 1),
    ([3,6,14,10], 4),
    ([2,3,5,12,18], 2),
    ([1,4,8,10,20], 3),
  ]
  rslts = [solver.minDistance(houses, k) for houses, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
