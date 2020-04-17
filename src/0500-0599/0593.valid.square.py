from typing import List

class Solution:
  def distSq(self, x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
  def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    d1 = self.distSq(p1, p2)
    d2 = self.distSq(p2, p3)
    d3 = self.distSq(p3, p4)
    d4 = self.distSq(p4, p1)
    d5 = self.distSq(p1, p3)
    d6 = self.distSq(p2, p4)
    d = sorted([d1,d2,d3,d4,d5,d6])
    return d[0] > 0 and d[0] * 2 == d[1] * 2 == d[2] * 2 == d[3] * 2 == d[4] == d[5]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0],[1,1],[1,0],[0,1]],
    [[1,0],[-1,0],[0,1],[0,-1]],
  ]
  rslts = [solver.validSquare(p1, p2, p3, p4) for p1, p2, p3, p4 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
