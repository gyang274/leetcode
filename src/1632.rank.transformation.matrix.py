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
  def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])
    # ranks matrix
    ranks = [[0] * n for _ in range(m)]
    # rr, rc: max rank seen on rows and cols
    rr, rc = [0] * m, [0] * n
    # d: value -> [(i, j), ..]
    d = defaultdict(list)
    for i in range(m):
      for j in range(n):
        d[matrix[i][j]].append((i, j))
    # assign rank by value sorted to increase
    for v in sorted(d.keys()):
      for i, j in d[v]:
        ranks[i][j] = max(rr[i] + 1, rc[j] + 1)
      if len(d[v]) > 1:
        # disjoint set union
        dsu = DSU(reps = {(i, j): (i, j) for i, j in d[v]})
        # di: i -> j's, such that matrix[i][j1] == matrix[i][j2]
        di = defaultdict(list)
        # dj: j -> i's, such that matrix[i1][j] == matrix[i2][j]
        dj = defaultdict(list)
        for i, j in d[v]:
          di[i].append(j)
          dj[j].append(i)
        for i in di:
          for j in di[i]:
            dsu.union((i, di[i][0]), (i, j))
        for j in dj:
          for i in dj[j]:
            dsu.union((dj[j][0], j), (i, j))
        # each connected component of (i, j)s get max ranks within component
        cc = defaultdict(list)
        for x in d[v]:
          cc[dsu.find(x)].append(x)
        for k in cc:
          rk = max(ranks[i][j] for i, j in cc[k])
          for i, j in cc[k]:
            ranks[i][j] = rk
      for i, j in d[v]:
        rr[i] = ranks[i][j]
        rc[j] = ranks[i][j]
    return ranks

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # [[1,2],[2,3]]
    [[1,2],[3,4]],
    # [[2,1,4,6],[2,6,5,4],[5,2,4,3],[4,3,1,5]],
    [[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]],
    # [3,4,1,2,7],[9,5,3,10,8],[4,6,2,7,5],[7,9,8,1,6],[12,10,4,5,11]]
    [[-37,-26,-47,-40,-13],[22,-11,-44,47,-6],[-35,8,-45,34,-31],[-16,23,-6,-43,-20],[47,38,-27,-8,43]],
    [[2,-11,24,15,26,-31],[-48,-49,22,37,-36,-5],[6,5,-44,27,14,-27],[36,-17,-6,13,-12,27],[46,-3,-36,31,-14,-7],[-36,27,-14,41,-40,23]],
  ]
  rslts = [solver.matrixRankTransform(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
