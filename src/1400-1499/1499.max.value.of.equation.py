from typing import List
from collections import deque

class Solution:
  def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
    # f() = (yj + xj) + (yi - xi), since xj > xi
    # TC: O(N), SC: O(N), stack of (xi, yi) where (yi - xi) decreasing as xi increasing
    q, m = deque([]), float('-inf')
    for x, y in points:
      # use (x, y) as (xj, yj)
      s = y + x
      while q and x - q[0][0] > k:
        q.popleft()
      if q:
        m = max(m, s + q[0][1])
      # use (x, y) as (xi, yi)
      d = y - x
      while q and d >= q[-1][1]:
        q.pop()
      q.append((x, d))
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,0],[3,0],[9,2]], 3),
    ([[1,3],[2,0],[5,10],[6,-10]], 1),
  ]
  rslts = [solver.findMaxValueOfEquation(points, k) for points, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
