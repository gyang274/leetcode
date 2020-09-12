from typing import List
from collections import defaultdict

class DSU:
  def __init__(self):
    # representer
    self.reps = {}
  def add(self, x):
    self.reps[x] = x
  def find(self, x):
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def closedIsland(self, grid: List[List[int]]) -> int:
    # dsu: disjoint set union
    m, n, dsu = len(grid), len(grid[0]), DSU()
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 0:
          dsu.add((i, j))
          for di, dj in [(-1, 0), (0, -1)]:
            x, y = i + di, j + dj
            if x >= 0 and y >= 0 and grid[x][y] == 0:
              dsu.union((x, y), (i, j))
    # islands: head -> all lands
    islands = defaultdict(set)
    for x, y in dsu.reps:
      islands[dsu.find((x, y))].add((x, y))
    # num of closed islands
    count = 0
    for i, j in islands:
      xs = [x for x, y in islands[(i, j)]]
      ys = [y for x, y in islands[(i, j)]]
      count += ((min(xs) > 0) and (max(xs) < m - 1) and (min(ys) > 0) and (max(ys) < n - 1))
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]],
    [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]],
    [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]],
  ]
  rslts = [solver.closedIsland(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
