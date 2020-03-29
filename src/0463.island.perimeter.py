from typing import List

import operator

class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    dxdy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    perimeter = 0
    for x in range(len(grid)):
      for y in range(len(grid[x])):
        if grid[x][y] == 1:
          connected = 0
          for dx, dy in dxdy:
            i, j = x + dx, y + dy
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
              connected += 1
          perimeter += 4 - connected
    return perimeter

class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    """each 0 -> 1 or 1 -> 0 within row or col represents a perimeter 1.
    """
    return sum(sum(map(operator.ne, [0] + row, row + [0])) for row in grid + list(map(list, zip(*grid))))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [
      [1]
    ],
    [
      [0,1,0,0],
      [1,1,1,0],
      [0,1,0,0],
      [1,1,0,0],
    ],
  ]
  rslts = [solver.islandPerimeter(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
