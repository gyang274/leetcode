from typing import List

import itertools

class DSU:
  def __init__(self):
    # representer
    self.reps = {}
    self.rank = {}
  def add(self, x):
    # -> (head, rank)
    self.reps[x] = x
    self.rank[x] = 0
  def find(self, x):
    # path compression
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    # union by rank
    hX = self.find(x)
    hY = self.find(y)
    if not hX == hY:
      h = hY if self.rank[hX] < self.rank[hY] else hX
      if self.rank[hX] == self.rank[hY]:
        self.rank[h] += 1
      self.reps[hX] = h
      self.reps[hY] = h

class Solution:
  def regionsBySlashes(self, grid: List[str]) -> int:
    n = len(grid)
    # imagine each grid cell with -x- 4 subregions
    # subregions are connected if not have / or \
    # one cell:
    # \ 3 /
    # 0 x 2  
    # / 1 \
    dsu = DSU()
    for i in range(n):
      for j in range(n):
        for k in range(4):
          dsu.add((i, j, k))
        if grid[i][j] != "/":
          dsu.union((i, j, 0), (i, j, 1))
          dsu.union((i, j, 2), (i, j, 3))
        if grid[i][j] != "\\":
          dsu.union((i, j, 0), (i, j, 3))
          dsu.union((i, j, 1), (i, j, 2))
        if i - 1 >= 0:
          dsu.union((i - 1, j, 1), (i, j, 3))
        if j - 1 >= 0:
          dsu.union((i, j - 1, 2), (i, j, 0))
    return len(set(map(dsu.find, itertools.product(range(n), range(n), range(4)))))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [" /","/ "],
    ["//","/ "],
    ["//","//"],
    ["\\/","/\\"],
    ["/\\","\\/"],
    ["\\/\\ "," /\\/"," \\/ ","/ / "],
  ]
  rslts = [solver.regionsBySlashes(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
