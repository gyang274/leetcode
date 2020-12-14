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
  def canonical(self, island):
    minx, miny = map(min, zip(*island))
    return tuple(sorted([(x - minx, y - miny) for x, y in island]))
  def rotateReflect(self, island):
    rr = []
    for mi, mj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
      rr.append(self.canonical([(x * mi, y * mj) for x, y in island]))
      rr.append(self.canonical([(y * mi, x * mj) for x, y in island]))
    return set(rr)
  def numDistinctIslands2(self, grid: List[List[int]]) -> int:
    """Q0694
    """
    # disjoint set union
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
    # distinct islands
    islands = defaultdict(list)
    for k, v in dsu.reps.items():
      islands[dsu.find(v)].append(k)
    # distinct islands normalized w.r.t translation, rotation and relfection.
    islands = [sorted(islands[i]) for i in islands]
    seen, count = set([]), 0
    for island in islands:
      rr = self.rotateReflect(island)
      if not (seen & rr):
        count += 1
      seen |= (rr)
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0,1],[1,1,1]],
    [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]],
    [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]],
    [[1,1,1,0,0],[1,0,0,0,1],[0,1,0,0,1],[0,1,1,1,0]],
  ]
  rslts = [solver.numDistinctIslands2(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
