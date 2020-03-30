from typing import List

class Solution:
  def direction(self, x0, x1, x2):
    return ((x1[0] - x0[0]) * (x2[1] - x1[1]) - (x1[1] - x0[1]) * (x2[0] - x1[0]))
  def isConvex(self, points: List[List[int]]) -> bool:
    """O(N), vector x0 -> x1 and x1 -> x2 always in same direction.
    """
    d, n = None, len(points)
    for i in range(n):
      di = self.direction(points[i], points[(i + 1) % n], points[(i + 2) % n])
      if di == 0:
        continue
      elif not d:
        d = 1 if di > 0 else -1
      elif d * di < 0:
        return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0],[0,1],[1,1],[1,0]],
    [[0,0],[0,10],[10,10],[10,0],[5,5]],
  ]
  rslts = [solver.isConvex(points) for points in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")