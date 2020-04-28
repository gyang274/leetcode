from typing import List

class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # cc: connected components, list of nodes set
    cc = []
    for s, t in edges:
      fs = ft = -1
      for i, nodes in enumerate(cc):
        if s in nodes:
          fs = i
        if t in nodes:
          ft = i
      if fs == ft == -1:
        cc.append({s, t})
      elif fs == ft:
        return (s, t)
      elif fs > -1 and ft > -1:
        ns = cc.pop(max(fs, ft))
        nt = cc.pop(min(fs, ft))
        cc.append(ns | nt)
      elif fs > -1:
        cc[fs].add(t)
      else:
        cc[ft].add(s)

class DSU:
  def __init__(self, size):
    # representer
    self.reps = [i for i in range(size + 1)]
  def find(self, x):
    while not x == self.reps[x]:
      x = self.reps[x]
    return x
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # disjoint set union
    dsu = DSU(len(edges))
    for x, y in edges:
      if dsu.find(x) == dsu.find(y):
        return (x, y)
      dsu.union(x, y)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2],[1,3],[2,3]],
    [[1,2],[2,3],[3,4],[1,4],[1,5]],
    [[3,4],[1,2],[2,4],[3,5],[2,5]],
  ]
  rslts = [solver.findRedundantConnection(edges) for edges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

