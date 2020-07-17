from typing import List

import string

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
  def equationsPossible(self, equations: List[str]) -> bool:
    # disjoint set union
    dsu = DSU(reps={x: x for x in string.ascii_lowercase})
    # parsing all == then !=
    es = []
    for e in equations:
      x1, x2, xequal = e[0], e[3], e[1:3] == '=='
      if x1 == x2:
        if not xequal:
          return False
      else:
        es.append((xequal, x1, x2))
    es.sort(reverse=True)
    for xequal, x1, x2 in es:
      if xequal:
        dsu.union(x1, x2)
      else:
        if dsu.find(x1) == dsu.find(x2):
          return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["a==b","b==a"],
    ["a==b","b!=a"],
    ["a==b","b==c","c==a"],
    ["a==b","b!=c","c==a"],
    ["c==c","b==d","x!=z"],
  ]
  rslts = [solver.equationsPossible(equations) for equations in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
