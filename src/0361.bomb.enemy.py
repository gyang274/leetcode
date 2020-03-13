from typing import List

class Solution:
  def maxKilledEnemies(self, grid: List[List[str]]) -> int:
    """dynamic programming
    """
    n = len(grid)
    if n == 0:
      return 0
    m = len(grid[0])
    if m == 0:
      return 0
    # enemy bombed w.r.t left, right, top, down
    dp = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    # row-wise
    for i in range(n):
      # left->right
      for j in range(1, m):
        if not grid[i][j-1] == "W":
          dp[i][j][0] = dp[i][j-1][0]
          if grid[i][j-1] == "E":
            dp[i][j][0] += 1
      # right->left
      for j in range(m - 2, -1, -1):
        if not grid[i][j+1] == "W":
          dp[i][j][1] = dp[i][j+1][1]
          if grid[i][j+1] == "E":
            dp[i][j][1] += 1
    # col-wise
    for j in range(m):
      # top->down
      for i in range(1, n):
        if not grid[i-1][j] == "W":
          dp[i][j][2] = dp[i-1][j][2]
          if grid[i-1][j] == "E":
            dp[i][j][2] += 1
      # down->top
      for i in range(n - 2, -1, -1):
        if not grid[i+1][j] == "W":
          dp[i][j][3] = dp[i+1][j][3]
          if grid[i+1][j] == "E":
            dp[i][j][3] += 1
    # xmax
    xmax = 0
    for i in range(n):
      for j in range(m):
        if grid[i][j] == "0":
          xmax = max(xmax, sum(dp[i][j]))
    return xmax

class Solution:
  def maxKilledEnemies(self, grid: List[List[str]]) -> int:
    n = len(grid)
    if n == 0:
      return 0
    m = len(grid[0])
    if m == 0:
      return 0
    rowhit, colhit = 0, [0] * m
    xmax = 0
    for i in range(n):
      for j in range(m):
        # expand row-wise to foresee enemy between walls in same row
        if j == 0 or grid[i][j - 1] == "W":
          rowhit = 0
          for k in range(j, m):
            if grid[i][k] == "W":
              break
            if grid[i][k] == "E":
              rowhit += 1
        # expand row-wise to foresee enemy between walls in same row
        if i == 0 or grid[i - 1][j] == "W":
          colhit[j] = 0
          for k in range(i, n):
            if grid[k][j] == "W":
              break
            if grid[k][j] == "E":
              colhit[j] += 1
        # xmax
        if grid[i][j] == "0":
          xmax = max(xmax, rowhit + colhit[j])
    return xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      ["0","E","0","0"],
      ["E","0","W","E"],
      ["0","E","0","0"]
    ],
  ]
  rslts = [solver.maxKilledEnemies(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")