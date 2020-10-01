from typing import List

class Solution:
  def countNegatives(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    # count the negative by reuse previous w.r.t sort
    count, e = 0, n
    for i in range(m):
      count += n - e
      for j in range(e - 1, -1, -1):
        if grid[i][j] < 0:
          count += 1
        else:
          e = j + 1
          break
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[4,3,2,0],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
  ]
  rslts = [solver.countNegatives(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
