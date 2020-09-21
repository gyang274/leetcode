from typing import List
from functools import lru_cache

class Solution:
  @lru_cache(None)
  def tilingRectangle(self, n: int, m: int) -> int:
    n, m = min(n, m), max(n, m)
    if m == n:
      return 1
    if m % n == 0:
      return m // n
    # split on one axis
    s1 = m * n
    for x in range(1, m // 2 + 1):
      s1 = min(s1, self.tilingRectangle(n, x) + self.tilingRectangle(n, m - x))
    for y in range(1, n // 2 + 1):
      s1 = min(s1, self.tilingRectangle(y, m) + self.tilingRectangle(n - y, m))
    # split on both axis
    s2 = m * n
    #    <-- yL -->
    #    --------------------------
    #    |        |_______________| xR
    #    |________|__rc__|        |
    # xL |               |        |
    #    --------------------------
    #                      <- yR ->
    # rc: self.tilingRectangle(n - yL - yR, m - xL - xR)
    for xL in range(1, m // 2 + 1):
      for xR in range(1, m - xL):
        for yL in range(1, n // 2 + 1):
          for yR in range(1, n - yL):
            s2 = min(
              s2, 
              self.tilingRectangle(n - yR, xL) +
              self.tilingRectangle(yL, m - xL) +
              self.tilingRectangle(n - yL, xR) +
              self.tilingRectangle(yR, m - xR) +
              self.tilingRectangle(n - yL - yR, m - xL - xR)
            )
    return min(s1, s2)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3),
    (3, 5),
    (5, 8),
    (9, 10),
    (11, 13),
  ]
  rslts = [solver.tilingRectangle(n, m) for n, m in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
