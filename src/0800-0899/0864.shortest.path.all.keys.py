from typing import List
from collections import deque

class Solution:
  def shortestPathAllKeys(self, grid: List[str]) -> int:
    """TC: O(K N^2), modified bfs or a-star search.
    """
    # modified bfs
    # init m, n, lock, keys, queue, seen
    # queue is list of (keys on hand, position, steps)
    m, n = len(grid), len(grid[0])
    lock, keys = set(), set()
    for i in range(m):
      for j in range(n):
        if grid[i][j] == '@':
          queue, seen = deque([((), i, j, 0)]), {((), i, j)}
        elif grid[i][j] not in {'.', '#'}:
          if grid[i][j].islower():
            keys.add(grid[i][j])
          else:
            lock.add(grid[i][j])
    # main
    # NOTE: a-star search, priority queue with lower bound of min distance to all keys
    # prioritize the search to make it more efficient on average, but not the worst case.
    while queue:
      k, i, j, s = queue.popleft()
      for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x, y = i + di, j + dj
        if 0 <= x < m and 0 <= y < n and grid[x][y] != '#' and (k, x, y) not in seen:
          if grid[x][y] in lock and grid[x][y].lower() not in k:
            continue
          knext = k[:]
          if grid[x][y] in keys and grid[x][y] not in k:
            knext += (grid[x][y], )
            if len(knext) == len(keys):
              return s + 1
          seen.add((knext, x, y))
          queue.append((knext, x, y, s + 1))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["@.a.#","###.#","b.A.B"],
    ["@..aA","..B#.","....b"],
    [".#.b.","A.#aB","#d...","@.cC.","D...#"],
  ]
  rslts = [solver.shortestPathAllKeys(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
