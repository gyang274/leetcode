from typing import List

import itertools

class Solution:
  def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    magic = lambda a, b, c, d, e, f, g, h, i: (
      sorted([a,b,c,d,e,f,g,h,i]) == list(range(1, 10)) and (
        a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15
      )
    )
    count = 0
    for i in range(m - 2):
      for j in range(n - 2):
        if grid[i + 1][j + 1] == 5:
          if magic(
            grid[i][j], grid[i][j+1], grid[i][j+2],
            grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
            grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2],
          ):
            count += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[4,3,8,4],[9,5,1,9],[2,7,6,2]],
  ]
  rslts = [solver.numMagicSquaresInside(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
