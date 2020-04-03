from typing import List

import heapq

class Solution:
  def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
    """Dijkstra Algorithm.
    """
    n = len(maze)
    if n == 0:
      return "impossible"
    m = len(maze[0])
    if m == 0:
      return "impossible"
    fdist = {}
    moves = [(-1, 0, "u"), (0, 1, "r"), (1, 0, "d"), (0, -1, "l")]
    queue = [(0, "", 0, ball[0], ball[1]), (0, "", 1, ball[0], ball[1])]
    while queue:
      # (x, y) with mindist to explore moved from z direction
      xyzdist, xyzpath, z, x, y = heapq.heappop(queue)
      # next stoppage cell (i, j) w.r.t turn left or turn right
      for zz in [1, -1]:
        i, j, k, ijkdist = x, y, (z + zz) % 4, xyzdist
        dx, dy, dz = moves[k]
        if 0 <= i + dx < n and 0 <= j + dy < m and not maze[i + dx][j + dy]:
          ijkpath = xyzpath + dz
          while 0 <= i + dx < n and 0 <= j + dy < m and not maze[i + dx][j + dy]:
            i, j, ijkdist = i + dx, j + dy, ijkdist + 1
            if (i, j) not in fdist or ijkdist < fdist[(i, j)][0] or (ijkdist == fdist[(i, j)][0] and ijkpath < fdist[(i, j)][1]):
              fdist[(i, j)] = (ijkdist, ijkpath)
              # print(f"move: {(x, y)=} {ds}-> {(i, j)=}, {fdist[(i, j)]=}")
              if not (0 <= i + dx < n and 0 <= j + dy < m and not maze[i + dx][j + dy]):
                heapq.heappush(queue, (ijkdist, ijkpath, k, i, j))
    return "impossible" if tuple(hole) not in fdist else fdist[tuple(hole)][1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,1,0,0],[0,0,0,0],[1,0,0,1],[0,0,0,0]], [0,0], [3,3]),
    ([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]),
    ([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [1,2]),
    ([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1]),
    ([
      [0,1,0,0,1,0,0,1,0,0],
      [0,0,1,0,0,1,0,0,1,0],
      [0,0,0,0,0,0,1,0,0,1],
      [0,0,0,0,0,0,1,0,0,1],
      [0,1,0,0,1,0,0,1,0,0],
      [0,0,1,0,0,1,0,0,0,0],
      [0,0,0,0,0,0,1,0,0,0],
      [1,0,0,1,0,0,0,0,0,1],
      [0,1,0,0,1,0,0,1,0,0],
      [0,0,0,0,0,1,0,0,1,0]
    ], [2,4], [7,6]),
  ]
  rslts = [solver.findShortestWay(maze, ball, hole) for maze, ball, hole in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  