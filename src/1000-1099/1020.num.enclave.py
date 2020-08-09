from typing import List

class Solution:
  def numEnclaves(self, A: List[List[int]]) -> int:
    m, n = len(A), len(A[0])
    # bfs/dfs: init
    queue = []
    for i in range(m):
      if A[i][0] == 1:
        queue.append((i, 0))
      if A[i][n - 1] == 1:
        queue.append((i, n - 1))
    for j in range(1, n - 1):
      if A[0][j] == 1:
        queue.append((0, j))
      if A[m - 1][j] == 1:
        queue.append((m - 1, j))
    # bfs/dfs: main
    seen = set(queue)
    while queue:
      i, j = queue.pop()
      for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x, y = i + di, j + dj
        if 0 <= x < m and 0 <= y < n and A[x][y] == 1 and (x, y) not in seen:
          seen.add((x, y))
          queue.append((x, y))
    return sum(map(sum, A)) - len(seen)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]],
    [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]],
  ]
  rslts = [solver.numEnclaves(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
