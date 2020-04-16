from typing import List
from functools import cmp_to_key

class Solution:
  def anchor(self, points):
    imin, ymin = None, float("inf")
    for i in range(len(points)):
      y = points[i][1]
      if (y < ymin) or (y == ymin and points[i][0] < points[imin][0]):
        ymin = y
        imin = i
    return imin
  def compare(self, p1, p2):
    o12 = self.orientation(self.p0, p1, p2)
    if o12 == 0:
      return -(self.distSq(self.p0, p1) - self.distSq(self.p0, p2))
    return -o12
  def distSq(self, p0, p1):
    return abs(p1[0] - p0[0]) ** 2 + abs(p1[1] - p0[1]) ** 2
  def orientation(self, p0, p1, p2):
    """Q0469
      > 0, counter-clockwise, left turn
      = 0, colinear
      < 0, clockwise, right turn
    """
    return (p1[0] - p0[0]) * (p2[1] - p1[1]) - (p1[1] - p0[1]) * (p2[0] - p1[0])
  def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
    """convex hull: https://en.wikipedia.org/wiki/convex_hull_algorithms
     O(NH): gift wrapping/jarvis algorithm, O(NlogN): graham scan.
    """
    n = len(points)
    if n < 4:
      return points
    # O(N): point Po s.t., ymin and xmin in case of tie.
    i = self.anchor(points)
    points[0], points[i] = points[i], points[0]
    # O(NlogN): sort all points w.r.t to angle of PoPx w.r.t x-axis.
    self.p0 = points[0]
    points[1:] = sorted(points[1:], key=cmp_to_key(self.compare))
    # O(N): go through sorted Px, keep only left turn (P prev, C curr, N next), move forward each left turn.
    stack = [points[0], points[1]]
    k = 2
    while self.orientation(stack[0], stack[1], points[k]) == 0:
      stack.insert(1, points[k])
      k += 1
    for i in range(k, n):
      while len(stack) > 2 and self.orientation(stack[-2], stack[-1], points[i]) < 0:
        stack.pop()
      stack.append(points[i])
    return stack

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0],[1,0],[4,0]],
    [[0,0],[0,1],[1,1],[1,0]],
    [[0,0],[0,10],[10,10],[10,0],[5,5]],
    [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]],
    [[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0]]
    [[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
    [[0,2],[0,4],[0,5],[0,9],[2,1],[2,2],[2,3],[2,5],[3,1],[3,2],[3,6],[3,9],[4,2],[4,5],[5,8],[5,9],[6,3],[7,9],[8,1],[8,2],[8,5],[8,7],[9,0],[9,1],[9,6]]
  ]
  rslts = [solver.outerTrees(points) for points in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")