from functools import lru_cache

class Solution:
  @lru_cache(None)
  def numberOfSets(self, n: int, k: int) -> int:
    if n <= k:
      return 0
    if n == k + 1:
      return 1
    if k == 1:
      return n * (n - 1) // 2
    return (sum(self.numberOfSets(m, k - 1) for m in range(k, n)) + self.numberOfSets(n - 1, k)) % (10 ** 9 + 7)

import math

class Solution:
  def numberOfSets(self, n: int, k: int) -> int:
    return math.comb(n + k - 1, k * 2) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, 1),
    (3, 2),
    (4, 2),
    (5, 3),
    (8, 5),
    (30, 7),
    (751, 201),
  ]
  rslts = [solver.numberOfSets(n, k) for n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
