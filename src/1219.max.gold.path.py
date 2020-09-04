from typing import List
from collections import deque

class Solution:
  def getMaximumGold(self, grid: List[List[int]]) -> int:
    # bfs, use integer to hash positions of gold taken
    m, n = len(grid), len(grid[0])
    # init the queue, and hash of position
    q, d, k = deque([]), {}, 1
    for i in range(m):
      for j in range(n):
        if grid[i][j]:
          d[(i, j)] = 1 << k
          k += 1
          q.append((grid[i][j], i, j, d[(i, j)]))
    # bfs
    f = 0
    while q:
      g, i, j, h = q.popleft()
      f = max(f, g)
      for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x, y = i + di, j + dj
        if 0 <= x < m and 0 <= y < n and grid[x][y] and (not d[(x, y)] & h):
          q.append((g + grid[x][y], x, y, h | d[(x, y)]))
    return f

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,6,0],[5,8,7],[0,9,0]],
    [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,8]],
  ]
  rslts = [solver.getMaximumGold(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")