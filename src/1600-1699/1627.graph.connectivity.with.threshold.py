from typing import List

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
  def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
    if threshold == 0:
      return [True] * len(queries)
    dsu = DSU({i: i for i in range(1, n + 1)})
    for i in range(threshold + 1, n):
      k = 2
      while i * k <= n:
        dsu.union(i, i * k)
        k += 1
    return [dsu.find(i) == dsu.find(j) for i, j in queries]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (6, 2, [[1,4],[2,5],[3,6]]),
    (6, 0, [[4,5],[3,4],[3,2],[2,6],[1,3]]),
    (5, 1, [[4,5],[4,5],[3,2],[2,3],[3,4]]),
  ]
  rslts = [solver.areConnected(n, threshold, queries) for n, threshold, queries in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
