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

class DSU:
  def __init__(self, reps: dict = {}):
    # representer
    self.reps = reps
  def add(self, x):
    self.reps[x] = x
  def find(self, x):
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    # disjoint set union
    dsu = DSU(reps={})
    for i in range(m):
      for j in range(n):
        if grid[i][j] == "1":
          dsu.add((i, j))
          if i > 0 and grid[i][j] == grid[i - 1][j] == "1":
            dsu.union((i - 1, j), (i, j))
          if j > 0 and grid[i][j] == grid[i][j - 1] == "1":
            dsu.union((i, j - 1), (i, j))
    return len(set([dsu.find(k) for k in dsu.reps]))

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