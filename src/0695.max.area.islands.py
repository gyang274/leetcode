from typing import List
from collections import defaultdict

class DSU:
  def __init__(self):
    # representer
    self.reps = {}
  def add(self, x):
    self.reps[x] = x
  def find(self, x):
    while not x == self.reps[x]:
      x = self.reps[x]
    return x
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    # disjoint-union set
    m = len(grid)
    if m == 0:
      return 0
    n = len(grid[0])
    if n == 0:
      return 0
    dsu = DSU()
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          dsu.add((i, j))
          for di, dj in [(-1, 0), (0, -1)]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
              dsu.union((x, y), (i, j))
    islands = defaultdict(list)
    for k, v in dsu.reps.items():
      islands[dsu.find(v)].append(k)
    islands = [len(islands[i]) for i in islands]
    return max(islands) if islands else 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0,1],[1,1,1]],
    [[0,0,0,0,0,0,0,0]],
    [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]],
    [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]],
  ]
  rslts = [solver.maxAreaOfIsland(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

  
        