from typing import List
from collections import defaultdict

class DSU:
  def __init__(self, size):
    # representer
    self.reps = [i for i in range(size + 1)]
  def find(self, x):
    while not x == self.reps[x]:
      x = self.reps[x]
    return x
  def union(self, x, y):
    self.reps[self.find(x)] = self.find(y)

class Solution:
  def detectCycle(self, d, x, y):
    # x, y: initial edge x <- y, x is parent
    while x in d and not d[x][0] == y:
      x = d[x][0]
    if x in d and d[x][0] == y:
      return True
    else:
      return False
  def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
    # d: hashmap for detect double parents
    d, z = defaultdict(list), 0
    for x, y in edges:
      if d[y]:
        z = y
      d[y].append(x)
    # case 1, cycle, no double parents
    if not z:
      dsu = DSU(len(edges))
      for x, y in edges:
        if dsu.find(x) == dsu.find(y):
          return (x, y)
        dsu.union(x, y)
    # case 2, no cycle, double parents
    else:
      for x in d[z]:
        # case 3, cycle and double parents
        # return the edge within the cycle
        if self.detectCycle(d, x, z):
          return (x, z)
      return (d[z][1], z)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2],[1,3],[2,3]],
    [[2,1],[3,1],[4,2],[1,4]],
    [[1,2],[2,3],[3,4],[1,4],[1,5]],
    [[5,2],[5,1],[3,1],[3,4],[3,5]],
  ]
  rslts = [solver.findRedundantDirectedConnection(edges) for edges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
