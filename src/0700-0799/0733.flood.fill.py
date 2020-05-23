from typing import List
from collections import deque

class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    """BFS/DFS
    """
    m, n = len(image), len(image[0])
    color, queue, seen = image[sr][sc], deque([(sr, sc)]), set([(sr, sc)])
    while queue:
      i, j = queue.popleft()
      image[i][j] = newColor
      for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x, y = i + di, j + dj
        if 0 <= x < m and 0 <= y < n and (x, y) not in seen and image[x][y] == color:
          seen.add((x, y))
          queue.append((x, y))
    return image

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2),
  ]
  rslts = [solver.floodFill(image, sr, sc, newColor) for image, sr, sc, newColor in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
