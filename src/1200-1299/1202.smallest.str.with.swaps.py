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
  def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    # dsu: disjoin set union
    dsu = DSU(reps={i: i for i in range(len(s))})
    for i, j in pairs:
      dsu.union(i, j)
    # grp: head -> groups of index swapable
    grp = defaultdict(set)
    for i in range(len(s)):
      grp[dsu.find(i)].add(i)
    # make the smallest str
    seen, r = set(), [None] * len(s)
    for i in range(len(s)):
      if i not in seen:
        ik = grp[dsu.find(i)]
        for j, x in zip(sorted(ik), sorted(s[j] for j in ik)):
          r[j] = x
        seen |= ik
    return ''.join(r)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("dcab", [[0,3],[1,2]]),
    ("dcab", [[0,3],[1,2],[0,2]]),
  ]
  rslts = [solver.smallestStringWithSwaps(s, pairs) for s, pairs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
