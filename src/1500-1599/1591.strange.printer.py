from typing import List
from collections import defaultdict

class Solution:
  def isPrintable(self, grid: List[List[int]]) -> bool:
    m, n = len(grid), len(grid[0])
    # d: digit -> (row range, col range, cells, count of *)
    d = defaultdict(lambda: [m, -1, n, -1, set(), 0])
    for i in range(m):
      for j in range(n):
        d[grid[i][j]][0] = min(d[grid[i][j]][0], i)
        d[grid[i][j]][1] = max(d[grid[i][j]][1], i)
        d[grid[i][j]][2] = min(d[grid[i][j]][2], j)
        d[grid[i][j]][3] = max(d[grid[i][j]][3], j)
        d[grid[i][j]][4].add((i, j))
    # reverse remove, add back to others possible covered as *
    while d:
      # r: remove
      r = set()
      for x in d:
        if (d[x][1] - d[x][0] + 1) * (d[x][3] - d[x][2] + 1) == len(d[x][4]) + d[x][5]:
          r.add(x)
      if not r:
        return False
      for x in r:
        _, _, _, _, cs, _ = d.pop(x)
        for y in d:
          # rectangle overlap area, refr Q0223
          for i, j in cs:
            if d[y][0] <= i <= d[y][1] and d[y][2] <= j <= d[y][3]:
              d[y][5] += 1
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,1,1],[3,1,3]],
    [[1,2,1],[2,1,2],[1,2,1]],
    [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]],
    [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]],
  ]
  rslts = [solver.isPrintable(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
