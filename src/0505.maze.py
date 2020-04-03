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
  def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    """BFS
    """
    self.maze = maze
    self.n = len(maze)
    if self.n == 0:
      return -1
    self.m = len(maze[0])
    if self.m == 0:
      return -1
    self.init = tuple(start)
    self.ende = tuple(destination)
    self.dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if self.mission_impossible():
      return -1
    self.dist = {}
    self.dist[self.init] = 0
    queue = deque([(self.init[0], self.init[1], 0, 0), (self.init[0], self.init[1], 1, 0)])
    while queue:
      x, y, d, ddist = queue.popleft()
      if (x, y) not in self.dist or ddist <= self.dist[(x, y)]:
        # next stoppage cell w.r.t turn left or turn right.
        for dd in [1, -1]:
          i, j, k, dist = x, y, (d + dd) % 4, ddist
          dx, dy = self.dxdy[k][0], self.dxdy[k][1]
          while 0 <= i + dx < self.n and 0 <= j + dy < self.m and not self.maze[i + dx][j + dy]:
            i, j, dist = i + dx, j + dy, dist + 1
          if (i, j) not in self.dist or dist < self.dist[(i, j)]:
            self.dist[(i, j)] = dist
            queue.append((i, j, k, dist))
    return -1 if self.ende not in self.dist else self.dist[self.ende]

class Solution:
  def mission_impossible(self):
    x, y = self.ende
    # impossible if 4 neighbour cells are all 0s, or all 1s.
    # impossible if left/right 1s, up/down 0s, or up/down 0s, left/right 1s
    ns = ""
    for dx, dy in self.dxdy:
      ns += str(self.maze[x + dx][y + dy]) if 0 <= x + dx < self.n and 0 <= y + dy < self.m else "1"
    return ns in {"0000", "1111", "0101", "1010"}
  def backtrack(self, x, y, d, ddist):  
    for dd in [1, -1]:
      i, j, k, dist = x, y, (d + dd) % 4, ddist
      dx, dy = self.dxdy[k][0], self.dxdy[k][1]
      while 0 <= i + dx < self.n and 0 <= j + dy < self.m and not self.maze[i + dx][j + dy]:
        i, j, dist = i + dx, j + dy, dist + 1
      if (i, j) not in self.dist or dist < self.dist[(i, j)]:
        self.dist[(i, j)] = dist
        self.backtrack(i, j, k, dist)
  def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    """DFS
    """
    self.maze = maze
    self.n = len(maze)
    if self.n == 0:
      return -1
    self.m = len(maze[0])
    if self.m == 0:
      return -1
    self.init = tuple(start)
    self.ende = tuple(destination)
    # if self.init == self.ende:
    #   return 0
    self.dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if self.mission_impossible():
      return -1
    self.dist = {}
    self.dist[self.init] = 0
    self.backtrack(*start, 0, 0)
    self.backtrack(*start, 1, 0)
    return -1 if self.ende not in self.dist else self.dist[self.ende]

import heapq

class Solution:
  def mission_impossible(self):
    x, y = self.ende
    # impossible if 4 neighbour cells are all 0s, or all 1s.
    # impossible if left/right 1s, up/down 0s, or up/down 0s, left/right 1s
    ns = ""
    for dx, dy in self.dxdy:
      ns += str(self.maze[x + dx][y + dy]) if 0 <= x + dx < self.n and 0 <= y + dy < self.m else "1"
    return ns in {"0000", "1111", "0101", "1010"}
  def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    """Dijkstra Algorithm.
    """
    self.maze = maze
    self.n = len(maze)
    if self.n == 0:
      return -1
    self.m = len(maze[0])
    if self.m == 0:
      return -1
    self.init = tuple(start)
    self.ende = tuple(destination)
    self.dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if self.mission_impossible():
      return -1
    # Dijkstra Algorithm
    self.dist = {}
    self.dist[self.init] = 0
    queue = [(0, 0, self.init[0], self.init[1]), (0, 1, self.init[0], self.init[1])]
    while queue:
      # (x, y) with mindist to explore
      ddist, d, x, y = heapq.heappop(queue)
      # next stoppage cell w.r.t turn left or turn right.
      for dd in [1, -1]:
        i, j, k, dist = x, y, (d + dd) % 4, ddist
        dx, dy = self.dxdy[k][0], self.dxdy[k][1]
        while 0 <= i + dx < self.n and 0 <= j + dy < self.m and not self.maze[i + dx][j + dy]:
          i, j, dist = i + dx, j + dy, dist + 1
        if (i, j) not in self.dist or dist < self.dist[(i, j)]:
          self.dist[(i, j)] = dist
          heapq.heappush(queue, (dist, k, i, j))
    return -1 if self.ende not in self.dist else self.dist[self.ende]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,1,0,0],[0,0,0,0],[1,0,0,1],[0,0,0,0]], [0,0], [3,3]),
    ([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]),
    ([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [1,2]),
  ]
  rslts = [solver.shortestDistance(maze, start, destination) for maze, start, destination in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  