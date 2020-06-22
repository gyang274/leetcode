from typing import List

class Solution:
  def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    # grid[i][j] = min(max(row[i]), max(col[j]))
    m, n, r, c = 0, len(grid), list(map(max, grid)), list(map(max, zip(*grid)))
    for i in range(n):
      for j in range(n):
        m += min(r[i], c[j]) - grid[i][j]
    return m