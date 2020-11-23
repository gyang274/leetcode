from typing import List
from collections import defaultdict

class Solution:
  def uvseparator(self, u, v):
    # make sure v is not neighborur of u
    vs, q = set([v]), set([v])
    # bfs
    while q:
      qq = set()
      for x in q:
        for y in self.graph[x]:
          if y not in vs and y != u:
            vs.add(y)
            qq.add(y)
      q = qq
    return len(self.graph[u] & vs)
  def minDays(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    self.graph = defaultdict(set)
    self.nodes = []
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          self.nodes.append((i, j))
          for di, dj in [(-1, 0), (0, -1)]:
            x, y = i + di, j + dj
            if 0 <= x and 0 <= y and grid[x][y] == 1:
              self.graph[(i, j)].add((x, y))
              self.graph[(x, y)].add((i, j))
    x = float('inf')
    for i, u in enumerate(self.nodes):
      for v in self.nodes[(i + 1):]:
        if v not in self.graph[u]:
          x = min(x, self.uvseparator(u, v))
    return x if x < float('inf') else len(self.nodes)

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
  def numConnectedComponents(self, grid):
    m, n = len(grid), len(grid[0])
    # disjoint set union
    dsu = DSU()
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          dsu.add((i, j))
          for di, dj in [(-1, 0), (0, -1)]:
            x, y = i + di, j + dj
            if 0 <= x and 0 <= y and grid[x][y] == 1:
              dsu.union((x, y), (i, j))
    # islands: connected components
    islands = defaultdict(set)
    for x in dsu.reps:
      islands[dsu.find(x)].add(x)
    return len(islands)
  def minDays(self, grid: List[List[int]]) -> int:
    # key: at most 2 days to disconnect
    # 0 if disconnect, 1 if disconnect by 1, 2 otherwise
    # TC: O(M^2 N^2), SC: O(MN), brute force with dsu
    if self.numConnectedComponents(grid) != 1:
      return 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          grid[i][j] = 0
          if self.numConnectedComponents(grid) != 1:
            return 1
          grid[i][j] = 1
    return 2

class Solution:
  def minDays(self, grid: List[List[int]]) -> int:
    # key: at most 2 days to disconnect
    # 0 if disconnect, 1 if disconnect by 1, 2 otherwise
    # TC: O(MN), using Articulation Points, refr Q1192.
    # Articulation Points: 
    #  A vertex in an undirected connected graph is an articulation point (or cut vertex) iff removing it 
    #  (and edges through it) disconnects the graph.
    #  https://codeforces.com/blog/entry/71146
    #  https://en.wikipedia.org/wiki/Biconnected_component
    #  https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
    return NotImplemented

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,1,1,0],[0,1,1,0],[0,0,0,0]],
    [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]],
    [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1]],
    [[1,1,0,0,1,1,0,1,0,1,1,1,1],[1,1,0,1,0,1,1,0,1,1,1,0,0],[0,0,1,1,1,0,0,1,1,1,1,0,0],[1,1,1,0,1,0,1,1,1,1,1,1,1],[1,1,1,0,1,1,0,1,1,1,1,0,1],[0,0,1,1,1,1,1,1,1,1,0,1,1],[1,1,1,0,0,1,1,1,0,1,1,1,1],[0,1,1,1,1,1,1,1,1,0,1,0,0],[1,1,1,1,1,1,1,1,0,0,1,0,1],[1,0,1,1,1,1,0,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,0,1],[1,1,0,1,1,0,1,0,1,1,1,1,0],[1,0,1,1,1,1,1,1,1,1,1,0,1],[1,1,0,1,1,1,1,0,1,1,0,1,1],[1,0,1,1,1,1,1,1,1,1,1,0,1]],
    [[1,1,0,0,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,0,1],[1,0,1,1,0,1,1,1,1,1,1,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,0,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
  ]
  rslts = [solver.minDays(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
