from typing import List
from collections import defaultdict

class DSU:
  def __init__(self):
    self.reps = {}
  def add(self, x):
    self.reps[x] = x
  def find(self, x):
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def removeStones(self, stones: List[List[int]]) -> int:
    # dsu
    dsu, r, c = DSU(), defaultdict(list), defaultdict(list)
    for i, j in stones:
      dsu.add((i, j))
      if i in r:
        dsu.union((i, r[i][0]), (i, j))
      if j in c:
        dsu.union((c[j][0], j), (i, j))
      r[i].append(j)
      c[j].append(i)
    return len(stones) - len(set(map(dsu.find, map(tuple, stones))))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0]],
    [[0,0],[0,2],[1,1],[2,0],[2,2]],
    [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]],
  ]
  rslts = [solver.removeStones(stones) for stones in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
