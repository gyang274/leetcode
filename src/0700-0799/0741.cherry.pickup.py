from typing import List

class Solution:
  def cherryPickup(self, grid: List[List[int]]) -> int:
    """dynamic programming, O(N^3)
      use 2 person pick, move (0, 0) -> (n - 1, n - 1), down or right, one pass,
      at each step s, person1 (r1, c1) and person2 at (r2, c2) must have s = r1 + c1 = r2 + c2
      so c2 = r1 + c1 - r2, e.g, r1, c1, r2 determines c2, so only need consider (r1, c1, r2).
    """
    n = len(grid)
    dp = [[[float('-inf')] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    for r1 in range(n - 1, -1, -1):
      for c1 in range(n - 1, -1, -1):
        for r2 in range(min(n - 1, r1 + c1), max(-1, r1 + c1 - n), -1):
          c2 = r1 + c1 - r2
          if grid[r1][c1] == -1 or grid[r2][c2] == -1:
            continue
          else:
            dp[r1][c1][r2] = grid[r1][c1] + (r1 != r2) * grid[r2][c2]
            if r1 + c1 < (n - 1) * 2:
              dp[r1][c1][r2] += max(
                # person 1 move down, person 2 move down
                dp[r1 + 1][c1][r2 + 1],
                # person 1 move down, person 2 move right
                dp[r1 + 1][c1][r2],
                # person 1 move right, person 2 move down
                dp[r1][c1 + 1][r2 + 1],
                # person 1 move right, person 2 move right
                dp[r1][c1 + 1][r2],
              )
    return max(0, dp[0][0][0])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # [[0,1,-1],[1,0,-1],[1,1,1]],
    # [[1,1,-1],[1,-1,1],[-1,1,1]],
    # [[0,1,1,1],[0,1,-1,-1],[0,-1,1,1],[1,0,0,0]],
    # [[0,1,1,0,0],[1,1,1,1,0],[-1,1,1,1,-1],[0,1,1,1,0],[1,0,-1,0,0]],
    [[1,1,-1,1,1],[1,1,1,1,1],[-1,1,1,-1,-1],[0,1,1,-1,0],[1,0,-1,1,0]],
    # [[1,-1,-1,-1,-1],[1,0,1,-1,-1],[0,-1,1,0,1],[1,0,1,1,0],[-1,-1,-1,1,1]],
  ]
  rslts = [solver.cherryPickup(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
