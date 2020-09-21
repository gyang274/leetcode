from typing import List

import heapq

class Solution:
  def minimumMoves(self, grid: List[List[int]]) -> int:
    # bfs, dfs, a-star search
    # A-star search with heuristic: h(Hr, Hc, Hd, Tr, Tc) = (Tr - Hr) + (Tc - Hc) + Hd
    # where Hr, Hc is the snake head position and Hd is the snake head direction,
    #  Hd == 0 when snake is horizontal, e.g., snake takes (Hr, Hc - 1), (Hr, Hc)
    #  Hd == 1 when snake lays vertical, e.g., snake takes (Hr - 1, Hc), (Hr, Hc)
    # and Tx and Ty are target position
    n = len(grid)
    if not grid[n - 1][n - 2] == grid[n - 1][n - 1] == 0:
      return -1
    # q: (e = d + h, d: moves, h: heuristic as lower bound to target, Hr, Hc, Hd)
    q, seen = [(2 * n - 3, 0, 2 * n - 3, 0, 1, 0)], {}
    while q:
      e, d, h, hr, hc, hd = heapq.heappop(q)
      if (hr, hc, hd) == (n - 1, n - 1, 0):
        return d
      if (hr, hc, hd) not in seen:
        seen[(hr, hc, hd)] = d
        # move to next w.r.t position and direction
        if hd == 0:
          # snake is horizontal (hd == 0)
          if hc + 1 < n and grid[hr][hc + 1] == 0 and (hr, hc + 1, hd) not in seen:
            # move right
            heapq.heappush(q, (e, d + 1, h - 1, hr, hc + 1, hd))
          if hr + 1 < n and grid[hr + 1][hc - 1] == grid[hr + 1][hc] == 0:
            if (hr + 1, hc, hd) not in seen:
              # move down
              heapq.heappush(q, (e, d + 1, h - 1, hr + 1, hc, hd))
            if (hr + 1, hc - 1, hd ^ 1) not in seen:
              # rotate clockwise
              heapq.heappush(q, (e + 2, d + 1, h + 1, hr + 1, hc - 1, hd ^ 1))
        else:
          # snake lays vertical (hd == 1)
          if hr + 1 < n and grid[hr + 1][hc] == 0 and (hr + 1, hc, hd) not in seen:
            # move down
            heapq.heappush(q, (e, d + 1, h - 1, hr + 1, hc, hd))
          if hc + 1 < n and grid[hr - 1][hc + 1] == grid[hr][hc + 1] == 0:
            if (hr, hc + 1, hd) not in seen:
              # move right
              heapq.heappush(q, (e, d + 1, h - 1, hr, hc + 1, hd))
            if (hr - 1, hc + 1, hd ^ 1) not in seen:
              # rotate counterclockwise
              heapq.heappush(q, (e, d + 1, h - 1, hr - 1, hc + 1, hd ^ 1))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
    [[0,0,0,0,0,1],[1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0]],
    [[0,0,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,0]],
  ]
  rslts = [solver.minimumMoves(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
