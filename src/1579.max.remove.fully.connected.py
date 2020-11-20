from typing import List
from collections import defaultdict

import copy

class DSU:
  def __init__(self, reps):
    # representer
    self.reps = reps
  # def add(self, x):
  #   self.reps[x] = x
  def find(self, x):
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    # start with all type3 edges
    es = [[], [], [], []]
    for i, u, v in edges:
      es[i].append((u, v))
    # start with all type3 edges
    dsu = DSU(reps = {x: x for x in range(1, n + 1)})
    for u, v in es[3]:
      dsu.union(u, v)
    # islands
    islands = defaultdict(set)
    for x in range(1, n + 1):
      islands[dsu.find(x)].add(x)
    if len(islands) == 1:
      return len(edges) - (n - 1)
    # Alice
    dA = copy.deepcopy(dsu)
    for u, v in es[1]:
      dA.union(u, v)
    islandsA = defaultdict(set)
    for x in range(1, n + 1):
      islandsA[dA.find(x)].add(x)
    if len(islandsA) > 1:
      return -1
    # Bruce
    dB = copy.deepcopy(dsu)
    for u, v in es[2]:
      dB.union(u, v)
    islandsB = defaultdict(set)
    for x in range(1, n + 1):
      islandsB[dB.find(x)].add(x)
    if len(islandsB) > 1:
      return -1
    return len(edges) - (n - len(islands)) - (len(islands) - 1) * 2

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # 2
    (4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4],[3,3,4]]),
    # 9
    (19, [[1,1,2],[2,1,2],[1,2,3],[2,2,3],[1,1,4],[2,1,4],[1,1,5],[2,1,5],[3,4,6],[3,3,7],[1,2,8],[2,2,8],[3,1,9],[1,3,10],[2,3,10],[1,8,11],[2,8,11],[1,5,12],[2,5,12],[1,8,13],[2,8,13],[3,10,14],[1,9,15],[2,9,15],[3,13,16],[3,9,17],[3,11,18],[1,1,19],[2,1,19],[2,4,10],[2,2,4],[2,3,18],[2,14,15],[1,4,17],[1,7,10],[1,6,14],[1,3,12],[1,5,14]]),
    # 33
    (12, [[3,1,2],[2,2,3],[3,1,4],[2,3,5],[1,2,6],[2,4,7],[3,3,8],[3,2,9],[2,1,10],[2,1,11],[1,11,12],[1,10,11],[2,5,9],[2,7,10],[2,4,12],[3,9,10],[1,6,9],[2,10,12],[1,2,5],[3,5,6],[1,7,11],[1,8,9],[1,1,11],[3,4,5],[1,5,9],[2,4,9],[1,8,11],[3,6,8],[1,8,10],[2,2,4],[2,3,8],[3,2,6],[3,10,11],[2,3,11],[3,5,9],[3,3,5],[2,6,11],[3,2,7],[1,5,11],[1,1,5],[2,9,10],[1,6,7],[3,2,3],[2,8,9],[3,2,8]]),
  ]
  rslts = [solver.maxNumEdgesToRemove(n, edges) for n, edges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
