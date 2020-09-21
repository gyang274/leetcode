from typing import List

class Solution:
  def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    def T(p0, p1):
      x, y = abs(p0[0] - p1[0]), abs(p0[1] - p1[1])
      return min(x, y) + abs(x - y)
    return sum(T(p0, p1) for p0, p1 in zip(points[:-1], points[1:]))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[2,3],[-2,2]],
    [[1,1],[3,4],[-1,0]],
  ]
  rslts = [solver.minTimeToVisitAllPoints(points) for points in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
