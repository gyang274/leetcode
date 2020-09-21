from typing import List

import heapq

class Solution:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    # a-star search
    # state: (heuristic + moves, moves, row, col, num obstacle removed)
    q, seen = [(m - 1 + n - 1 + 0, 0, 0, 0, 0)], set()
    while q:
      _, d, x, y, z = heapq.heappop(q)
      if (x, y) == (m - 1, n - 1):
        return d
      if (x, y, z) not in seen:
        seen.add((x, y, z))
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
          i, j = x + dx, y + dy
          if 0 <= i < m and 0 <= j < n:
            if grid[i][j] == 0:
              heapq.heappush(q, (m - 1 - i + n - 1 - j + d + 1, d + 1, i, j, z))
            elif z + 1 <= k:
              # grid[i][j] == 1
              heapq.heappush(q, (m - 1 - i + n - 1 - j + d + 1, d + 1, i, j, z + 1))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([
      [0,1,1],
      [1,1,1],
      [1,0,0]
    ], 1),
    ([
      [0,0,0],
      [1,1,0],
      [0,0,0],
      [0,1,1],
      [0,0,0]
    ], 1),
    ([
      [0,0,0],
      [1,1,0],
      [0,0,0],
      [0,1,1],
      [0,0,0]
    ], 2),
  ]
  rslts = [solver.shortestPath(grid, k) for grid, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
