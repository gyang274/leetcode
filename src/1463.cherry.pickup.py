from typing import List
from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, i, j1, j2):
    ans = x12 = self.x[i][j1] if j1 == j2 else (self.x[i][j1] + self.x[i][j2])
    if i + 1 < self.m:
      for d1, d2 in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
        k1, k2 = j1 + d1, j2 + d2
        if 0 <= k1 < self.n and 0 <= k2 < self.n:
          ans = max(ans, x12 + self.recursive(i + 1, k1, k2))
    return ans
  def cherryPickup(self, grid: List[List[int]]) -> int:
    self.x, self.m, self.n = grid, len(grid), len(grid[0])
    self.recursive.cache_clear()
    return self.recursive(0, 0, self.n - 1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,1],[1,1]],
    [[3,1,1],[2,5,1],[1,5,5],[2,1,1]],
    [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]],
    [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]],
  ]
  rslts = [solver.cherryPickup(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
