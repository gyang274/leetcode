from typing import List

import heapq

class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    # bfs, dfs, A-star search
    # A-star search with heuristic h(p1, p2) = max(abs(x1 - x2), abs(y1 - y2))
    # heuristic specified as a lower bound of travelling distance between p1, p2, so that
    # when a solution found, then all other possible solutions must have longer distance.
    n = len(grid)
    if grid[0][0] == 1:
      return -1
    # source and target
    s, t = (0, 0), (n - 1, n - 1)
    # d: determined (x, y) -> distance
    # c: candidate (estimated-distance = heuristic-distance-to-t + determined-path-length-from-s, x, y)
    d, c = {}, [(n - 1, n - 1, 1, 0, 0)]
    while c:
      _, h, f, x, y = heapq.heappop(c)
      if (x, y) == t:
        return f
      if (x, y) not in d:
        d[(x, y)] = f
        for dx, dy in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
          u, v = x + dx, y + dy
          if 0 <= u < n and 0 <= v < n and grid[u][v] == 0 and (u, v) not in d:
            heapq.heappush(c, (n + f - min(u, v), n - 1 - min(u, v), f + 1, u, v))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,1],[1,0]],
    [[0,0,0],[1,1,0],[1,1,0]],
    [[1,0,0],[1,1,0],[1,1,0]],
  ]
  rslts = [solver.shortestPathBinaryMatrix(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
