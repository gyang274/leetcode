from typing import List
from collections import deque

class Solution:
  def mission_impossible(self):
    x, y = self.ende
    # impossible if 4 neighbour cells are all 0s, or all 1s.
    # impossible if left/right 1s, up/down 0s, or up/down 0s, left/right 1s
    ns = ""
    for dx, dy in self.dxdy:
      ns += str(self.maze[x + dx][y + dy]) if 0 <= x + dx < self.n and 0 <= y + dy < self.m else "1"
    return ns in {"0000", "1111", "0101", "1010"}
  def backtrack(self, x, y, d):
    for dd in [1, -1]:
      i, j, k = x, y, (d + dd) % 4
      dx, dy = self.dxdy[k][0], self.dxdy[k][1]
      while 0 <= i + dx < self.n and 0 <= j + dy < self.m and not self.maze[i + dx][j + dy]:
        i, j = i + dx, j + dy
      if (i, j) not in self.visited:
        self.visited.add((i, j))
        if (i, j) == self.ende:
          return True
        if self.backtrack(i, j, k):
          return True
    return False
  def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    """DFS
    """
    self.maze = maze
    self.n = len(maze)
    if self.n == 0:
      return False
    self.m = len(maze[0])
    if self.m == 0:
      return False
    self.init = tuple(start)
    self.ende = tuple(destination)
    self.dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if self.mission_impossible():
      return False
    self.visited = set([self.init])
    return self.backtrack(*start, 0) or self.backtrack(*start, 1)

class Solution:
  def mission_impossible(self):
    x, y = self.ende
    # impossible if 4 neighbour cells are all 0s, or all 1s.
    # impossible if left/right 1s, up/down 0s, or up/down 0s, left/right 1s
    ns = ""
    for dx, dy in self.dxdy:
      ns += str(self.maze[x + dx][y + dy]) if 0 <= x + dx < self.n and 0 <= y + dy < self.m else "1"
    return ns in {"0000", "1111", "0101", "1010"}
  def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    """BFS
    """
    self.maze = maze
    self.n = len(maze)
    if self.n == 0:
      return False
    self.m = len(maze[0])
    if self.m == 0:
      return False
    self.init = tuple(start)
    self.ende = tuple(destination)
    self.dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if self.mission_impossible():
      return False
    self.visited = set([self.init])
    queue = deque([(self.init[0], self.init[1], 0), (self.init[0], self.init[1], 1)])
    while queue:
      x, y, d = queue.popleft()
      # next stoppage cell w.r.t turn left or turn right.
      for dd in [1, -1]:
        i, j, k = x, y, (d + dd) % 4
        dx, dy = self.dxdy[k][0], self.dxdy[k][1]
        while 0 <= i + dx < self.n and 0 <= j + dy < self.m and not self.maze[i + dx][j + dy]:
          i, j = i + dx, j + dy
        if (i, j) not in self.visited:
          self.visited.add((i, j))
          if (i, j) == self.ende:
            return True
          queue.append((i, j, k))
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,1,0,0],[0,0,0,0],[1,0,0,1],[0,0,0,0]], [0,0], [3,3]),
    ([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]),
  ]
  rslts = [solver.hasPath(maze, start, destination) for maze, start, destination in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  