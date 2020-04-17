from typing import List

class Solution:
  def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
    """bfs
    """
    n = len(matrix)
    if n == 0:
      return []
    m = len(matrix[0])
    if m == 0:
      return [[]]
    queue = []
    for i in range(n):
      for j in range(m):
        if matrix[i][j] == 0:
          queue.append((i, j))
    dist, visited = 1, set(queue)
    while queue:
      bound = []
      while queue:
        x, y = queue.pop()
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
          i, j = x + dx, y + dy
          if 0 <= i < n and 0 <= j < m and (i, j) not in visited:
            visited.add((i, j))
            matrix[i][j] = dist
            bound.append((i, j))
      queue = bound
      dist += 1
    return matrix

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0,0],[0,1,0],[0,0,0]],
    [[0,0,0],[0,1,0],[1,1,1]],
  ]
  rslts = [solver.updateMatrix(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")