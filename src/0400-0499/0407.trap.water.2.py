from typing import List

import heapq

class Solution:
  def trapRainWater(self, heightMap: List[List[int]]) -> int:
    """Priority queue move the boundary to track water, O(4?mn). 
    """
    m = len(heightMap)
    if m < 3:
      return 0
    n = len(heightMap[0])
    if n < 3:
      return 0
    # push all boundary into a priority queue
    bound = []
    visit = set()
    w = 0
    for i in [0, m - 1]:
      for j in range(n):
        bound.append((heightMap[i][j], i, j))
        visit.add((i, j))
    for j in [0, n - 1]:
      for i in range(1, m - 1):
        bound.append((heightMap[i][j], i, j))
        visit.add((i, j))
    # heapify
    heapq.heapify(bound)
    # move bound
    hbnd = -1
    while bound:
      hmin, x, y = heapq.heappop(bound)
      hbnd = max(hbnd, hmin)
      dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
      for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if (not (0 <= nx < m and 0 <= ny < n)) or ((nx, ny) in visit):
          continue
        h = heightMap[nx][ny]
        if h < hbnd:
          w += hbnd - h
        heapq.heappush(bound, (h, nx, ny))
        visit.add((nx, ny))
        # print(f'visit: {nx=}, {ny=}, {h=}, {hbnd=}, {hmin=}, {w=}')
    return w

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [
      [1,4,3,1,3,2],
      [3,2,1,3,2,4],
      [2,3,3,2,3,1],
    ],
    [
      [12,13,1,12],
      [13,4,13,12],
      [13,8,10,12],
      [12,13,12,12],
      [13,13,13,13]
    ],
  ]
  rslts = [solver.trapRainWater(heightMap) for heightMap in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")