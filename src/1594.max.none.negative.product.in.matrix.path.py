from typing import List

from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, i, j):
    # x: max of positive
    # y: min of negative
    # zero
    if self.grid[i][j] == 0:
      return 0, 0
    # init
    if i == j == 0:
      return (self.grid[i][j], float('inf')) if self.grid[i][j] > 0 else (float('-inf'), self.grid[i][j])
    # ux, uy: max positive and min negative from upper
    ux, uy = float('-inf'), float('inf')
    if i - 1 >= 0:
      ux, uy = self.recursive(i - 1, j)
    # lx, ly: max positive and min negative from leftr
    lx, ly = float('-inf'), float('inf')
    if j - 1 >= 0:
      lx, ly = self.recursive(i, j - 1)
    # construct x, y
    if self.grid[i][j] > 0:
      x = max(ux, lx) * self.grid[i][j]
      y = min(uy, ly) * self.grid[i][j]
    else:
      y = max(ux, lx) * self.grid[i][j]
      x = min(uy, ly) * self.grid[i][j]
    return x, y
  def maxProductPath(self, grid: List[List[int]]) -> int:
    self.grid = grid
    m, n = len(grid), len(grid[0])
    x, y = self.recursive(m - 1, n - 1)
    self.recursive.cache_clear()
    return x % (10 ** 9 + 7) if x > float('-inf') else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1, 3],[0,-4]],
    [[1,-2,1],[1,-2,1],[3,-4,1]],
    [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]],
    [[1,4,4,0],[-2, 0,0,1],[1,-1,1,1]],
    # 19215865
    [[2,1,3,0,-3,3,-4,4,0,-4],[-4,-3,2,2,3,-3,1,-1,1,-2],[-2,0,-4,2,4,-3,-4,-1,3,4],[-1,0,1,0,-3,3,-2,-3,1,0],[0,-1,-2,0,-3,-4,0,3,-2,-2],[-4,-2,0,-1,0,-3,0,4,0,-3],[-3,-4,2,1,0,-4,2,-4,-1,-3],[3,-2,0,-4,1,0,1,-3,-1,-1],[3,-4,0,2,0,-2,2,-4,-2,4],[0,4,0,-3,-4,3,3,-1,-2,-2]],
  ]
  rslts = [solver.maxProductPath(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
