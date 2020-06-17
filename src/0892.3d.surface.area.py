from typing import List

class Solution:
  def surfaceAreaOneDirection(self, height):
    n = len(height)
    a, h = 0, [0] + list(height) + [0]
    for i in range(1, n + 1):
      a += max(0, h[i] - h[i - 1]) + max(0, h[i] - h[i + 1])
    return a
  def surfaceArea(self, grid: List[List[int]]) -> int:
    # Q0883
    xy = sum(map(lambda r: sum(map(lambda x: x > 0, r)), grid)) * 2
    xz = sum(map(self.surfaceAreaOneDirection, grid))
    yz = sum(map(self.surfaceAreaOneDirection, zip(*grid)))
    return xy + xz + yz

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[2]],
    [[1,2],[3,4]],
    [[1,0],[0,2]],
    [[1,1,1],[1,0,1],[1,1,1]],
    [[2,2,2],[2,1,2],[2,2,2]],
  ]
  rslts = [solver.surfaceArea(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
