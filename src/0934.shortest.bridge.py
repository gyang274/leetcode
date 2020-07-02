from typing import List
from collections import defaultdict, deque

class DSU:
  def __init__(self):
    # representer
    self.reps = {}
  def add(self, x):
    self.reps[x] = x
  def find(self, x):
    while not x == self.reps[x]:
      x = self.reps[x]
    return x
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def shortestBridge(self, A: List[List[int]]) -> int:
    n = len(A)
    # connected components as islands
    dsu = DSU()
    for i in range(n):
      for j in range(n):
        if A[i][j] == 1:
          dsu.add((i, j))
          for di, dj in [(-1, 0), (0, -1)]:
            x, y = i + di, j + dj
            if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
              dsu.union((x, y), (i, j))
    islands = defaultdict(set)
    for u, v in dsu.reps:
      islands[dsu.find((u, v))].add((u, v))
    # verify len(islands) == 2
    # shortest bridge between A and B
    A, B = set(islands.popitem()[1]), set(islands.popitem()[1])
    # bfs A -> B
    queue, seen, dest = deque([(i, j, 0) for i, j in A]), A, B
    while queue:
      i, j, d = queue.popleft()
      for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x, y = i + di, j + dj
        if (x, y) in dest:
          return d
        if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
          seen.add((x, y))
          queue.append((x, y, d + 1))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,1],[1,0]],
    [[0,1,0],[0,0,0],[0,0,1]],
    [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]],
  ]
  rslts = [solver.shortestBridge(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
