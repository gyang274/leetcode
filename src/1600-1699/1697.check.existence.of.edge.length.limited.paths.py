from typing import List

class DSU:
  def __init__(self, reps: dict = {}):
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
  def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
    # sort the queries by increasing limit O(NlogN)
    # disjoint set union over edges <= (increasing) limit O(N)
    # e: sorted edges by decreasing distance
    e = sorted([(d, u, v) for u, v, d in edgeList], reverse=True)
    # q: sorted queries by increasing limits
    q = sorted([(x[2], i, x[0], x[1]) for i, x in enumerate(queries)])
    # s: answer
    s = [None] * len(q)
    # dsu
    dsu = DSU(reps={x:x for x in range(n)})
    for l, i, u, v in q:
      while e and e[-1][0] < l:
        _, x, y = e.pop()
        dsu.union(x, y)
      s[i] = (dsu.find(u) == dsu.find(v))
    return s
