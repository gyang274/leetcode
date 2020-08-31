from typing import List

import copy

class Solution:
  def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
    # step1, O(N^2), dp, count the consecutive 1s start at (i, j) to top, left, down, right, (t, l, d, r)
    # step2, O(N^3), straightforward, at (i, j), take (i + k, j + k), for k in range(1, min(d,r)-at-(i,j)), 
    #  see if min(t,l)-at-(i+k, j+k) >= k for k-square, often, k is limited and early break, so the overall
    #  performance is expected to be close to O(N^2) instead of O(N^3).
    m, n = len(grid), len(grid[0])
    # tldr: 4 x m x n
    tldr = [copy.deepcopy(grid) for _ in range(4)]
    for i in range(m):
      for j in range(n):
        if grid[i][j]:
          if i:
            tldr[0][i][j] = tldr[0][i - 1][j] + 1
          if j:
            tldr[1][i][j] = tldr[1][i][j - 1] + 1
    for j in range(n - 1, -1, -1):
      for i in range(m - 1, -1, -1):
        if grid[i][j]:
          if i + 1 < m:
            tldr[2][i][j] = tldr[2][i + 1][j] + 1
          if j + 1 < n:
            tldr[3][i][j] = tldr[3][i][j + 1] + 1
    # diagonal only
    mk = 0
    for i in range(m):
      for j in range(n):
        k0 = 0 if i == 0 or j == 0 else min(tldr[2][i - 1][j - 1], tldr[3][i - 1][j - 1])
        for k in range(min(tldr[2][i][j], tldr[3][i][j]) - 1, k0 - 1, -1):
          if min(tldr[0][i + k][j + k], tldr[1][i + k][j + k]) >= k:
            mk = max(mk, k + 1)
            break
    return mk * mk

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,0,0,1]],
    [[1,1,0,0]],
    [[0,0],[0,0]],
    [[1,1,1],[1,0,1],[1,1,1]],
  ]
  rslts = [solver.largest1BorderedSquare(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
