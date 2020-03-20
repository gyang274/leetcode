from typing import List

import heapq

class Solution:
  def _oceanTide(self, bound, visit):
    """find ocean reachable locations.
    """
    ans = visit.copy()
    # make bound as priority queue
    heapq.heapify(bound)
    # move along the boundary
    hbnd = -1
    while bound:
      hmin, x, y = heapq.heappop(bound)
      hbnd = max(hbnd, hmin)
      for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        i, j = x + dx, y + dy
        if (i, j) not in visit:
          visit.add((i, j))
          if 0 <= i < self.n and 0 <= j < self.m and self.matrix[i][j] >= hbnd:
            heapq.heappush(bound, (self.matrix[i][j], i, j))
            ans.add((i, j))
    return ans
  def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    if n == 0:
      return []
    m = len(matrix[0])
    if m == 0:
      return []
    self.matrix, self.n, self.m = matrix, n, m
    # push all boundary go pacific
    bound, visit = [], set([])
    for i in range(n):
      bound.append((matrix[i][0], i, 0))
      visit.add((i, 0))
    for j in range(m):
      bound.append((matrix[0][j], 0, j))
      visit.add((0, j))
    ansPa = self._oceanTide(bound, visit)
    # push all boundary go atlantic
    bound, visit = [], set([])
    for i in range(n):
      bound.append((matrix[i][m - 1], i, m - 1))
      visit.add((i, m - 1))
    for j in range(m):
      bound.append((matrix[n - 1][j], n - 1, j))
      visit.add((n - 1, j))
    ansAt = self._oceanTide(bound, visit)
    return ansPa & ansAt

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      [1,2,3],
      [8,9,4],
      [7,6,5]
    ],
    [
      [1,2,2,3,5],
      [3,2,3,4,4],
      [2,4,5,3,1],
      [6,7,1,4,5],
      [5,1,1,2,4]
    ],
  ]
  rslts = [solver.pacificAtlantic(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
