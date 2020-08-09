from typing import List

class Solution:
  def isBoomerang(self, points: List[List[int]]) -> bool:
    # triangleArea(x1, y1, x2, y2, x3, y3)
    #       |     |- x1 y1 1 -| |
    # 1/2 * | det |  x2 y2 1  | |
    #       |     |_ x3 y3 1 _| |
    (x1, y1), (x2, y2), (x3, y3) = points
    return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,1],[2,3],[3,2]],
    [[1,1],[2,2],[3,3]],
  ]
  rslts = [solver.isBoomerang(points) for points in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
