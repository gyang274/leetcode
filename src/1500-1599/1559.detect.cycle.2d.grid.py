from typing import List

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
  def containsCycle(self, grid: List[List[str]]) -> bool:
    # detect cycle, often dfs, but use dsu in this problem due to its special graph structure.
    m, n = len(grid), len(grid[0])
    dsu = DSU()
    for i in range(m):
      for j in range(n):
        dsu.add((i, j))
        if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j] == grid[i][j - 1] == grid[i][j] and dsu.find((i - 1, j)) == dsu.find((i, j - 1)):
          return True
        if i - 1 >= 0 and grid[i - 1][j] == grid[i][j]:
          dsu.union((i - 1, j), (i, j))
        if j - 1 >= 0 and grid[i][j - 1] == grid[i][j]:
          dsu.union((i, j - 1), (i, j))
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [["a","b","b"],["b","z","b"],["b","b","a"]],
    [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]],
    [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]],
  ]
  rslts = [solver.containsCycle(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
