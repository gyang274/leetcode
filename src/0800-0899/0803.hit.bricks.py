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
  def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    """O(N∗Q∗α(N∗Q)), where N = R * C grid squares, Q hits, and α is the Inverse-Ackermann function.
      Key: instead of looking at the graph as a series of sequential cuts, one shall look at the graph after all cuts,
        and reverse each cut and keep tracking num of connected components after each reversion.
    """
    n = len(grid)
    if n == 0:
      return []
    m = len(grid[0])
    if m == 0:
      return []
    # mark out all hits as done
    for i, j in hits:
      grid[i][j] *= -1
    # dsu: connected components
    dsu = DSU()
    for i in range(n):
      for j in range(m):
        if grid[i][j] == 1:
          dsu.add((i, j))
          for di, dj in [(-1, 0), (0, -1)]:
            x, y = i + di, j + dj
            if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                dsu.union((x, y), (i, j))
    # hits and fall
    ans = []
    for i, j in hits[::-1]:
      ans.append(0)
      if grid[i][j] == -1:
        grid[i][j] *= -1
        dsu.add((i, j))
        # union on exists components, derive fall reversely
        hs = set([])
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
          x, y = i + di, j + dj
          if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
            hs.add(dsu.find((x, y)))
        if hs:
          hs = sorted(hs)
          if i == 0 and hs[0][0] > 0:
            ans[-1] += dsu.size[hs[0]]
          dsu.union(hs[0], (i, j))
          while len(hs) > 1:
            if hs[0][0] == 0 and hs[-1][0] > 0:
              ans[-1] += dsu.size[hs[-1]]
            dsu.union(hs[0], hs[-1])
            hs.pop()
    return ans[::-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,0,0,0],[1,1,1,0]], [[1,0]]),
    ([[1,0,0,0],[1,1,0,0]], [[1,1],[1,0]]),
    ([[1,0,0,0],[1,1,1,0]], [[1,1],[1,0]]),
    ([[1,0,1],[1,1,1]], [[0,0],[0,2],[1,1]]),
  ]
  rslts = [solver.hitBricks(grid, hits) for grid, hits in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
