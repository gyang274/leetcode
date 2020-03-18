from typing import List

import copy

class Solution:
  def shortestDistance(self, grid: List[List[int]]) -> int:
    """BFS from each 1 to every 0, want 0 minimize sum of distance.
    """
    # n = len(grid)
    # if n == 0:
    #   return 0
    # m = len(grid[0])
    # if m == 0:
    #   return 0
    n, m = len(grid), len(grid[0])
    # preprocessing
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # build adjacent zeros can be done in processing 1st building dist so that
    # the script is more efficient O(N) instead O(5N) in preprocessing but less elegant
    # ones: set of (x, y) where grid[x][y] == 1
    # nbrs: dict key by (x, y) where grid[x][y] = 0 or 1, value of (x + dx, y + dy) where grid[x + dx][y + dy] = 0 or 1
    ones, nbrs = set([]), {}
    for x in range(n):
      for y in range(m):
        if grid[x][y] < 2:
          if grid[x][y] == 1:
            ones.add((x, y))
          nbrs[(x, y)] = set([])
          for dx, dy in dxdy:
            i, j = x + dx, y + dy
            if 0<= i < n and 0 <= j < m and grid[i][j] < 2:
              nbrs[(x, y)].add((i, j))
    # any 0
    n1s = len(ones)
    if len(nbrs) == n1s:
      return -1
    # dist: distance from each 1 to all 0s
    dist = [copy.deepcopy(grid) for _ in range(n1s)]
    # k: index of 1 (building)
    k = 0
    while ones:
      zdist, boundary, extended, reachables = 0, set([ones.pop(), ]), set([]), set([])
      while boundary:
        zdist += 1
        while boundary:
          x, y = boundary.pop()
          for i, j in nbrs[(x, y)]:
            if dist[k][i][j] == 0:
              # an unvisited cell
              dist[k][i][j] = zdist
              extended.add((i, j))
            if grid[i][j] == 1:
              reachables.add((i, j))
        boundary, extended = extended, set([])
      # only need on the 1st one
      if not len(reachables) == n1s:
        return -1
      k += 1
    mindist = (n * m) * n1s
    for x, y in nbrs:
      if grid[x][y] == 0:
        z = 0
        for k in range(n1s):
          if dist[k][x][y] > 0:
            # (x, y) is reachable from k-th 1 (building)
            z += dist[k][x][y]
          else:
            z = (n * m) * n1s
        mindist = min(z, mindist)
    return mindist if mindist < (n * m) * n1s else -1

class Solution:
  def bfs(self, x, y):
    ones, sumdists = self.ones.copy(), 0
    dist, boundary, extended, unvisited = 0, set([(x, y), ]), set([]), set(self.nbrs.keys()).difference(set([(x, y), ]))
    while boundary:
      dist += 1
      while boundary:
        x, y = boundary.pop()
        for i, j in self.nbrs[(x, y)]:
          if (i, j) in ones:
            ones.remove((i, j))
            sumdists += dist
          elif (i, j) in unvisited:
            unvisited.remove((i, j))
            extended.add((i, j))
      boundary, extended = extended, set([])
    if ones:
      return -1
    return sumdists
  def shortestDistance(self, grid: List[List[int]]) -> int:
    """BFS from each 0 to all 1s if possible, find the zero lead to shortest distance overall.
    """
    n, m = len(grid), len(grid[0])
    # preprocessing
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # build adjacent zeros can be done in processing 1st building dist so that
    # the script is more efficient O(N) instead O(5N) in preprocessing but less elegant
    # ones: set of (x, y) where grid[x][y] == 1
    # nbrs: dict key by (x, y) where grid[x][y] = 0, value of (x + dx, y + dy) where grid[x + dx][y + dy] == 0
    self.ones, self.nbrs = set([]), {}
    for x in range(n):
      for y in range(m):
        if grid[x][y] == 0:
          self.nbrs[(x, y)] = set([])
          for dx, dy in dxdy:
            i, j = x + dx, y + dy
            if 0<= i < n and 0 <= j < m and grid[i][j] < 2:
              self.nbrs[(x, y)].add((i, j))
        if grid[x][y] == 1:
          self.ones.add((x, y))
    # init mindist with a large enough number
    mindist = (n * m) * len(self.ones)
    for x, y in self.nbrs:
      dist = self.bfs(x, y)
      if dist > 0:
        mindist = min(dist, mindist)
    return mindist if mindist < (n * m) * len(self.ones) else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      [1,0,2,0,1],
      [0,0,0,0,0],
      [0,0,1,0,0]
    ],
    [
      [1,1,1,1,1,0],
      [0,0,0,0,0,1],
      [0,1,1,0,0,1],
      [1,0,0,1,0,1],
      [1,0,1,0,0,1],
      [1,0,0,0,0,1],
      [0,1,1,1,1,0]
    ]
  ]
  rslts = [solver.shortestDistance(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")