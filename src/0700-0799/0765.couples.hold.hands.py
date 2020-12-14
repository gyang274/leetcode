from typing import List
from collections import defaultdict

class DSU:
  def __init__(self, reps: dict = {}):
    # representer
    self.reps = reps
  def add(self, x):
    self.reps[x] = x
  def find(self, x):
    while not x == self.reps[x]:
      x = self.reps[x]
    return x
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def minSwapsCouples(self, row: List[int]) -> int:
    """O(N)
      suppose couple i (2i, 2i + 1) seats on X and Y, connect X // 2 and Y // 2, stable at N self-connected components
      each swap reduces 1 edge and introduces 1 self-connected component from a cycle, so that a cycle size s requires
      s - 1 swaps, as a result, init m cycles -> n - m swaps.
    """
    n = len(row)
    # disjoint set union 
    # seat index // 2 as node
    dsu = DSU(reps={i: i for i in range(n // 2)})
    # couples seats X, Y
    # connect X // 2, Y // 2 as edge
    d = defaultdict(list)
    for i, p in enumerate(row):
      d[p // 2].append(i // 2)
    for p in d:
      dsu.union(*d[p])
    # connect components
    cc = defaultdict(list)
    for k, v in dsu.reps.items():
      cc[dsu.find(v)].append(k)
    return n // 2 - len(cc)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0,2,1,3],
    [0,2,4,6,3,5,7,1],
  ]
  rslts = [solver.minSwapsCouples(row) for row in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
