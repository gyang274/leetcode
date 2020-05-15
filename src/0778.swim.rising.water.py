from typing import List

import heapq

class Solution:
  def swimInWater(self, grid: List[List[int]]) -> int:
    n, t = len(grid), 0
    seen, queue = {(0, 0)}, [(grid[0][0], 0, 0)]
    while queue:
      s, i, j = heapq.heappop(queue)
      t = max(s, t)
      if i == j == n - 1:
        return t
      for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x, y = i + di, j + dj
        if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
          seen.add((x, y))
          heapq.heappush(queue, (grid[x][y], x, y))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,2],[3,1]],
    [[0,2],[1,3]],
    [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]],
  ]
  rslts = [solver.swimInWater(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
