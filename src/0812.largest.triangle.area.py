from typing import List

import itertools

class Solution:
  def largestTriangleArea(self, points: List[List[int]]) -> float:
    # TODO: Q0587: get convex hull and consider points on convex hull only?
    area = lambda p, q, r: .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]-p[1]*q[0]-q[1]*r[0]-r[1]*p[0])
    return max(area(*triangle) for triangle in itertools.combinations(points, 3))
