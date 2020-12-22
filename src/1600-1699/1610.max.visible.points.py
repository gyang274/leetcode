from typing import List
from collections import deque

import math

class Solution:
  def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
    # TC: O(NlogN), SC: O(N)
    u, v = location
    # d: angle of each point w.r.t location as origin, o: num of points at origin.
    d, o = [], 0
    for x, y in points:
      if x == u and y == v:
        o += 1
      else:
        d.append(math.atan2(y - v, x - u) / math.pi * 180)
    # sort w.r.t angle
    d.sort()
    # circle around
    d = d + [r + 360 for r in d]
    # count within point of view
    m, q = 0, deque([])
    for x in d:
      while q and x - q[0] > angle:
        q.popleft()
      q.append(x)
      m = max(m, len(q))
    return m + o

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,0],[2,1]], 23, [1,1]),
    ([[2,1],[2,2],[3,3]], 90, [1,1]),
    ([[2,1],[2,2],[3,4],[1,1]], 90, [1,1]),
  ]
  rslts = [solver.visiblePoints(points, angle, location) for points, angle, location in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
