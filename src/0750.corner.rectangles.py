from typing import List

class Solution:
  def countCornerRectangles(self, grid: List[List[int]]) -> int:
    n = len(grid)
    # corners
    d = {}
    for i in range(n):
      d[i] = set([i for i,x in enumerate(grid[i]) if x])
    # rectangles
    count = 0
    for j in range(n):
      for i in range(j):
        m = len(d[i] & d[j])
        count += m * (m - 1) // 2
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,1,0],[1,0,1],[1,0,1],[0,1,0]],
  ]
  rslts = [solver.countCornerRectangles(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
