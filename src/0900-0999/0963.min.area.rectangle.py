from typing import List
from collections import defaultdict

import itertools

class Solution:
  def minAreaFreeRect(self, points: List[List[int]]) -> float:
    # a necessary and sufficient condition to form a rectangle 
    # with two opposite pairs of points is that the points must 
    # have the same center and radius.
    points = list(map(lambda z: complex(*z), points))
    # d: (center, radius) => [(p, q), ..] 
    d = defaultdict(list)
    for p, q in itertools.combinations(points, 2):
      center = (p + q) / 2
      radius = abs(center - p)
      d[(center, radius)].append((p, q))
    # (p1, q1), (p2, q2) with same (center, radius) determines rectangle
    ans = float('inf')
    for (center, radius) in d:
      for (p1, q1), (p2, q2) in itertools.combinations(d[(center, radius)], 2):
        ans = min(ans, abs(p1 - p2) * abs(p1 - (2 * center - p2)))
    return ans if ans < float('inf') else 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,1],[1,0],[1,2],[2,1]],
    [[0,3],[1,2],[3,1],[1,3],[2,1]],
    [[0,0],[0,1],[1,0],[1,1],[2,1],[2,0]],
    [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]],
  ]
  rslts = [solver.minAreaFreeRect(points) for points in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
