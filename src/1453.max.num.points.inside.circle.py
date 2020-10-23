from typing import List

import itertools

class Solution:
  def numPoints(self, points: List[List[int]], r: int) -> int:
    # http://www4.comp.polyu.edu.hk/~csbxiao/paper/2004/ISPAN04_cover.pdf
    # TC: O(N^3), possible O(N^2logN), SC: O(1)
    ans = 1
    for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
      d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) / 4.0
      if d <= r * r:
        x0 = (x1 + x2) / 2.0 + (y2 - y1) * (r * r - d) ** 0.5 / (d * 4) ** 0.5
        y0 = (y1 + y2) / 2.0 - (x2 - x1) * (r * r - d) ** 0.5 / (d * 4) ** 0.5
        ans = max(ans, sum((x - x0) ** 2 + (y - y0) ** 2 <= r * r + 0.00001 for x, y in points))
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[-2,0],[2,0],[0,2],[0,-2]], 2),
    ([[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], 2),
    ([[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], 5),
  ]
  rslts = [solver.numPoints(points, r) for points, r in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
