from typing import List
from collections import deque

class Solution:
  def maxDistance(self, grid: List[List[int]]) -> int:
    # bfs, start with all lands, expand to water wrt min distance
    n, q, seen = len(grid), deque([]), set()
    for i in range(n):
      for j in range(n):
        if grid[i][j]:
          q.append((i, j, 0))
          seen.add((i, j))
    n2 = n ** 2
    if not q or len(seen) == n2:
      return -1
    while q and len(seen) < n2:
      i, j, d = q.popleft()
      for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x, y = i + di, j + dj
        if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
          q.append((x, y, d + 1))
          seen.add((x, y))
    return q[-1][-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0]],
    [[1]],
    [[1,0,1],[0,0,0],[1,0,1]],
    [[1,0,0],[0,0,0],[0,0,0]],
  ]
  rslts = [solver.maxDistance(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

