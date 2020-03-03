from typing import List
from statistics import median

class Solution:
  def minTotalDistance(self, grid: List[List[int]]) -> int:
    """O(N): (x_median, y_median).
    """
    xs, ys = [], []
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 1:
          xs.append(i)
          ys.append(j)
    dist = 0
    if xs and ys:
      xm, ym = int(median(xs)), int(median(ys))
      dist = sum([abs(x - xm) for x in xs]) + sum([abs(y - ym) for y in ys])
    return dist

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [[]],
    [[1,1]],
    [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]],
  ]
  rslts = [solver.minTotalDistance(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

