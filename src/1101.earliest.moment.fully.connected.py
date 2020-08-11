from typing import List

class DSU:
  def __init__(self, reps: dict = {}, size: dict = {}):
    self.reps = reps
    self.size = size
  def find(self, x):
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    hX = self.find(x)
    hY = self.find(y)
    if not hX == hY:
      self.reps[hY] = hX
      self.size[hX] += self.size[hY]
      self.size.pop(hY)
    return self.size[hX]

class Solution:
  def earliestAcq(self, logs: List[List[int]], N: int) -> int:
    # O(NlogN) sort
    logs.sort()
    # DSU
    dsu = DSU(reps={x: x for x in range(N)}, size={x: 1 for x in range(N)})
    # O(Nlog*(N))
    for t, x, y in logs:
      s = dsu.union(x, y)
      if s == N:
        return t
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6),
  ]
  rslts = [solver.earliestAcq(logs, N) for logs, N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
