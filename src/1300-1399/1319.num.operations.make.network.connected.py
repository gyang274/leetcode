from typing import List
from collections import defaultdict

class DSU:
  def __init__(self, reps):
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
  def makeConnected(self, n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
      return -1
    # dsu
    dsu = DSU(reps={i: i for i in range(n)})
    for u, v in connections:
      dsu.union(u, v)
    # islands
    islands = defaultdict(set)
    for i in range(n):
      islands[dsu.find(i)].add(i)
    return len(islands) - 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [[0,1],[0,2],[1,2]]),
    (5, [[0,1],[0,2],[2,3],[3,4]]),
    (6, [[0,1],[0,2],[0,3],[1,2]]),
    (6, [[0,1],[0,2],[0,3],[1,2],[1,3]]),
  ]
  rslts = [solver.makeConnected(n, connections) for n, connections in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
