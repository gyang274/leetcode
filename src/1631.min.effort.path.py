from typing import List

import heapq

class Solution:
  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    m, n = len(heights), len(heights[0])
    # q: (e, x, y)
    q, visited, seen, emax = [(0, 0, 0)], set(), {(0, 0): 0}, 0
    while q:
      e, x, y = heapq.heappop(q)
      emax = max(emax, e)
      if x == m - 1 and y == n - 1:
        return emax
      if (x, y) not in visited:
        visited.add((x, y))
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
          i, j = x + dx, y + dy
          if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
            k = abs(heights[i][j] - heights[x][y])
            if (i, j) not in seen or k < seen[(i, j)]:
              heapq.heappush(q, (k, i, j))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2,2],[3,8,2],[5,3,5]],
    [[1,2,3],[3,8,4],[5,3,5]],
    [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],
  ]
  rslts = [solver.minimumEffortPath(heights) for heights in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
