from typing import List

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
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    # MST, minimum spanning tree, O(ElogV), Kruskal’s Algorithm
    n = len(points)
    # d: distance, e.g., graph edge weights
    def dist(i, j):
      return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
    d = sorted([(dist(i, j), i, j) for i in range(n) for j in range(i + 1, n)], reverse=True)
    # m: num of connected components, c: cost of connecting points
    m, c, dsu = n, 0, DSU(reps={i: i for i in range(n)})
    while m > 1:
      k, i, j = d.pop()
      if dsu.find(i) == dsu.find(j):
        continue
      dsu.union(i, j)
      m -= 1
      c += k
    return c

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0]],
    [[-10,-10],[10,10]],
    [[3,12],[-2,5],[-4,1]],
    [[0,0],[1,1],[1,0],[-1,1]],
    [[0,0],[2,2],[3,10],[5,2],[7,0]],
  ]
  rslts = [solver.minCostConnectPoints(points) for points in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
