from typing import List
from collections import defaultdict

class Solution:
  def _dist2(self, p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
  def numberOfBoomerangs(self, points: List[List[int]]) -> int:
    # cd: (center, distance) -> num of points
    cd = defaultdict(lambda: 0)
    for i in range(len(points)):
      for j in range(i + 1, len(points)):
        d = self._dist2(points[i], points[j])
        cd[(i, d)] += 1
        cd[(j, d)] += 1
    return sum([cd[k] * (cd[k] - 1) for k in cd])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0],[1,0],[2,0]],
  ]
  rslts = [solver.numberOfBoomerangs(points) for points in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")