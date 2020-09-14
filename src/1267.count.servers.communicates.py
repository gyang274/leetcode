from typing import List
from collections import defaultdict
from itertools import chain

class Solution:
  def countServers(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    d = defaultdict(set)
    for i in range(m):
      for j in range(n):
        if grid[i][j]:
          d[(0, i)].add((i, j))
          d[(1, j)].add((i, j))
    return len(set(chain.from_iterable(d[k] for k in d if len(d[k]) > 1)))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,0],[0,1]],
    [[1,0],[1,1]],
    [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]],
  ]
  rslts = [solver.countServers(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
