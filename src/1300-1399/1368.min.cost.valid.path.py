from typing import List

import heapq

class Solution:
  def minCost(self, grid: List[List[int]]) -> int:
    # a-star search
    m, n = len(grid), len(grid[0])
    # q: [(cost, -(i+j), i, j), ..]
    q, seen = [(0, 0, 0, 0)], set()
    while q:
      cost, _, i, j = heapq.heappop(q)
      if (i, j) == (m - 1, n - 1):
        return cost
      if (i, j) not in seen:
        seen.add((i, j))
        for dd, (di, dj) in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)]):
          x, y = i + di, j + dj
          if 0 <= x < m and 0 <= y < n:
            if dd == grid[i][j] - 1:
              if (x, y) == (m - 1, n - 1):
                return cost
              heapq.heappush(q, (cost, -(x + y), x, y))
            else:
              heapq.heappush(q, (cost + 1, -(x + y), x, y))
    return -1      

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1]],
    [[4]],
    [[1,2],[4,3]],
    [[2,2],[4,3]],
    [[2,2,2],[2,2,2]],
    [[1,1,3],[3,2,2],[1,1,4]],
    [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]],
  ]
  rslts = [solver.minCost(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
