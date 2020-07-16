from typing import List

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    # modified bfs
    fresh, rotten = set(), set()
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          fresh.add((i, j))
        if grid[i][j] == 2:
          rotten.add((i, j))
    queue, days = set(rotten), 0
    while fresh and queue:
      bound = set()
      days += 1
      for i, j in queue:
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
          x, y = i + di, j + dj
          if 0 <= x < m and 0 <= y < n and (x, y) in fresh:
            fresh.remove((x, y))
            rotten.add((x, y))
            bound.add((x, y))
      queue = bound
    return -1 if fresh else days

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0]],
    [[0,2]],
    [[2,1,1],[1,1,0],[0,1,1]],
    [[2,1,1],[0,1,1],[1,0,1]],
  ]
  rslts = [solver.orangesRotting(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
