from typing import List

class Solution:
  def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    def shift(i, j):
      z = (i * n + j + k) % (m * n)
      return z // n, z % n
    ans = [[None] * n for _ in range(m)]
    for i in range(m):
      for j in range(n):
        x, y = shift(i, j)
        ans[x][y] = grid[i][j]
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,2,3],[4,5,6]], 1),
    ([[1,2,3],[4,5,6]], 2),
    ([[1,2,3],[4,5,6]], 3),
    ([[1,2,3],[4,5,6]], 5),
    ([[1,2],[3,4],[5,6]], 8),
  ]
  rslts = [solver.shiftGrid(grid, k) for grid, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
