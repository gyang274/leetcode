class Solution:
  def distance(self, x, y):
    # manhattan distance between x and y
    return abs(x[0] - y[0]) + abs(x[1] - y[1])
  def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
    distT = [self.distance(nut, tree) for nut in nuts]
    distS = [self.distance(nut, squirrel) for nut in nuts]
    distD = [dt - ds for dt, ds in zip(distT, distS)]
    return sum(distT) * 2 - max(distD)