from typing import List

class Solution:
  def uniquePathsIII(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    # use a real num be denote path "visited" nodes
    init, ende, d, k = None, None, {}, 0
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 0:
          d[(i, j)] = 1 << k
          k += 1 
        elif grid[i][j] == 1:
          init = (i, j)
        elif grid[i][j] == 2:
          ende = (i, j)
        else:
          continue
    full = (1 << k) - 1
    # bfs/dfs: init -> ende
    queue, count = [(*init, 0)], 0
    while queue:
      i, j, k = queue.pop()
      for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x, y = i + di, j + dj
        if 0 <= x < m and 0 <= y < n:
          if k == full and (x, y) == ende:
            count += 1
          elif grid[x][y] == 0 and (k & d[(x, y)]) == 0:
            queue.append((x, y, k | d[(x, y)]))
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,0],[0,2]],
    [[1,0],[2,0]],
    [[1,0,0],[0,0,0],[0,0,2]],
    [[1,0,0,0],[0,0,0,0],[0,0,0,2]],
    [[1,0,0,0],[0,0,0,0],[0,0,2,-1]],
  ]
  rslts = [solver.uniquePathsIII(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
