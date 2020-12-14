from typing import List

class DSU:
  def __init__(self):
    # representer
    self.reps = {}
    self.size = {}
  def add(self, x):
    self.reps[x] = x
    self.size[x] = 1
  def find(self, x):
    while not x == self.reps[x]:
      x = self.reps[x]
    return x
  def union(self, x, y):
    hX = self.find(x)
    hY = self.find(y)
    if not hX == hY:
      h = min(hX, hY)
      if h == hX:
        self.reps[hY] = h
        self.size[hX] += self.size[hY]
        self.size.pop(hY)
      else:
        self.reps[hX] = h
        self.size[hY] += self.size[hX]
        self.size.pop(hX)

class Solution:
  def largestIsland(self, grid: List[List[int]]) -> int:
    """Q0694, Q0695, Q0803. TC: O(N^2), SC: O(N^2).
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
    # max island size
    ms = max(dsu.size.values()) if dsu.size else 0
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 0:
          r, s = set([]), 0
          for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
              z = dsu.find((x, y))
              if z not in r:
                r.add(z)
                s += dsu.size[z]
          ms = max(ms, s + 1)
    return ms

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0],[0,0]],
    [[1,0],[0,0]],
    [[1,0],[0,1]],
    [[1,1],[0,1]],
    [[1,1],[1,1]],
  ]
  rslts = [solver.largestIsland(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
