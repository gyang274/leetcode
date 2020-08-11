from typing import List
from collections import defaultdict
from itertools import product

class DSU:
  def __init__(self, reps: dict = {}):
    # representer
    self.reps = reps
  def add(self, x):
    self.reps[x] = x
  def find(self, x):
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def maximumMinimumPath(self, A: List[List[int]]) -> int:
    m, n = len(A), len(A[0])
    # d: A[i][j] -> (i, j)
    d = defaultdict(set)
    for i in range(m):
      for j in range(n):
        d[A[i][j]].add((i, j))
    # disjoint-set union
    dsu = DSU(reps = {(i, j): (i, j) for i, j in product(range(m), range(n))})
    # keep joining cells until connected
    vs, seen = sorted(d.keys(), reverse=True), set()
    for v in vs:
      for (i, j) in d[v]:
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
          x, y = i + di, j + dj
          if (x, y) in seen:
            dsu.union((i, j), (x, y))
        seen.add((i, j))
      if dsu.find((0, 0)) == dsu.find((m - 1, n - 1)):
        return v
    return -1

import heapq

class Solution:
  def maximumMinimumPath(self, A: List[List[int]]) -> int:
    # O(RC), greedy, explore on current max unseen
    m, n, q = len(A), len(A[0]), [(-A[0][0], 0, 0)]
    while q:
      s, i, j = heapq.heappop(q)
      if (i, j) == (m - 1, n - 1):
        return -s
      for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x, y = i + di, j + dj
        if 0 <= x < m and 0 <= y < n and A[x][y] != -1:
          heapq.heappush(q, (max(s, -A[x][y]), x, y))
          A[x][y] = -1
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[5,4,5],[1,2,6],[7,4,6]],
    [[2,2,1,2,2,2],[1,2,2,2,1,2]],
    [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]],
  ]
  rslts = [solver.maximumMinimumPath(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
