from typing import List

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    """BFS with (un)visited and boundary, like in Dijkstra algorithm.
    """
    n = len(grid)
    if n == 0:
      return 0
    m = len(grid[0])
    if m == 0:
      return 0
    islands, bounary, unvisited = 0, set(), set([(i, j) for i in range(n) for j in range(m)])
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while unvisited:
      x, y = unvisited.pop()
      if grid[x][y] == "1":
        islands += 1
        bounary.add((x, y))
        while bounary:
          x, y = bounary.pop()
          for dx, dy in dxdy:
            i, j = x + dx, y + dy 
            if (i, j) in unvisited:
              unvisited.remove((i, j))
              if grid[i][j] == "1":
                bounary.add((i, j))
    return islands

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [[]],
    [["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]],
    [["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"]],
    [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],
    [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]],
  ]
  rslts = [solver.numIslands(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")