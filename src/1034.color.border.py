from typing import List

class Solution:
  def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    # bfs connected component
    queue, border, seen = [(r0, c0)], [], set([(r0, c0)])
    for x, y in queue:
      isBorder = False
      if x == 0 or x == m - 1 or y == 0 or y == n - 1:
        isBorder = True
      for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        r, c = x + dx, y + dy
        if 0 <= r < m and 0 <= c < n:
          if grid[r][c] != grid[x][y]:
            isBorder = True
          elif (r, c) not in seen:
            seen.add((r, c))
            queue.append((r, c))
      if isBorder:
        border.append((x, y))
    # color the border
    for r, c in border:
      grid[r][c] = color
    return grid

class Solution:
  def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    # bfs connected component
    queue, border, seen = [(r0, c0)], set(), set([(r0, c0)])
    for x, y in queue:
      for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        r, c = x + dx, y + dy
        if 0 <= r < m and 0 <= c < n and grid[r][c] == grid[x][y]:
          if (r, c) not in seen:
            seen.add((r, c))
            queue.append((r, c))
        else:
          border.add((x, y))
    # color the border
    for r, c in border:
      grid[r][c] = color
    return grid

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,1],[1,2]], 0, 0, 3),
    ([[1,2,2],[2,3,2]], 0, 1, 3),
    ([[1,1,1],[1,1,1],[1,1,1]], 1, 1, 2),
  ]
  rslts = [solver.colorBorder(grid, r0, c0, color) for grid, r0, c0, color in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
