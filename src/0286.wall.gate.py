from typing import List

class Solution:
  def wallsAndGates(self, rooms: List[List[int]]) -> None:
    """Do not return anything, modify rooms in-place instead.
      O(MN), find 0 positions + BFS.
    """
    n = len(rooms)
    if n == 0:
      return None
    m = len(rooms[0])
    if m == 0:
      return None
    # init bounday with gates (zeros), visited with walls (-1s)
    visited, boundary, extended = set([]), set([]), set([])
    for i in range(n):
      for j in range(m):
        if rooms[i][j] == 0:
          boundary.add((i, j))
        elif rooms[i][j] == -1:
          visited.add((i, j))
    # BFS from boundary
    dist = 1
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while boundary or extended:
      while boundary:
        i, j = boundary.pop()
        visited.add((i, j))
        for dx, dy in dxdy:
          x, y = i + dx, j + dy
          if 0 <= x < n and 0 <= y < m and (x, y) not in visited and (x, y) not in boundary:
            rooms[x][y] = dist
            extended.add((x, y))
      boundary, extended = extended, set([])
      dist += 1
    return None
        
if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [
      [2147483647,-1,0,2147483647],
      [2147483647,2147483647,2147483647,-1],
      [2147483647,-1,2147483647,-1],
      [0,-1,2147483647,2147483647]
    ],
    [
      [2147483647,-1,0,2147483647],
      [2147483647,2147483647,-1,-1],
      [2147483647,-1,2147483647,-1],
      [0,-1,2147483647,2147483647]
    ],
  ]
  rslts = [
    solver.wallsAndGates(rooms) for rooms in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")