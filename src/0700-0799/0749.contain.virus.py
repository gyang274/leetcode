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
  def containVirus(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dsu = DSU()
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          dsu.add((i, j))
          for di, dj in [(-1, 0), (0, -1)]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
              dsu.union((x, y), (i, j))
    walls = set([])
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def buildWalls(walls):
      # islands
      islands = defaultdict(list)
      for k, v in dsu.reps.items():
        islands[dsu.find(v)].append(k)
      # borders
      boarder = defaultdict(set)
      kmax, smax = None, None
      for k in islands:
        for (i, j) in islands[k]:
          for d, (di, dj) in enumerate(moves):
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and (x, y, d) not in walls and grid[x][y] == 0:
              boarder[k].add((x, y, d))
        s = len(set([(x, y) for x, y, _ in boarder[k]]))
        if not kmax or s > smax:
          kmax, smax = k, s
      # build walls
      walls |= boarder[kmax]
      # remove quarantined region
      for (i, j) in islands[kmax]:
        dsu.reps.pop((i, j))
      islands.pop(kmax)
      boarder.pop(kmax)
      # spreads the virus
      for k in boarder:
        ik, jk = islands[k][0]
        for x, y, _ in boarder[k]:
          grid[x][y] = 1
          dsu.add((x, y))
          dsu.union((ik, jk), (x, y))
          for d, (dx, dy) in enumerate(moves):
            i, j = x + dx, y + dy
            if 0 <= i < m and 0 <= j < n and (x, y, (d + 2) % 4) not in walls and grid[i][j] == 1:
              dsu.union((x, y), (i, j))
      return walls
    while dsu.reps:
      walls = buildWalls(walls)
    return len(walls)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,1,1],[1,0,1],[1,1,1]],
    [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]],
    [[1,0,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,0,1,0,0,0,0,0,0]],
    [[1,0,1,0,0,0,0,0,0,0],[1,0,1,0,0,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,0]],
    [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]],
    [
      [0,1,0,1,1,1,1,1,1,0],
      [0,0,0,1,0,0,0,0,0,0],
      [0,0,1,1,1,0,0,0,1,0],
      [0,0,0,1,1,0,0,1,1,0],
      [0,1,0,0,1,0,1,1,0,1],
      [0,0,0,1,0,1,0,1,1,1],
      [0,1,0,0,1,0,0,1,1,0],
      [0,1,0,1,0,0,0,1,1,0],
      [0,1,1,0,0,1,1,0,0,1],
      [1,0,1,1,0,1,0,1,0,1],
    ],
  ]
  rslts = [solver.containVirus(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
