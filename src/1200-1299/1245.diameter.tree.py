from typing import List
from collections import defaultdict

import heapq

class Solution:
  def recursive(self, node):
    ms = []
    for u in self.graph[node]:
      if u not in self.visited:
        self.visited.add(u)
        ms.append(self.recursive(u))
    if ms:
      self.diameter = max(self.diameter, sum(heapq.nlargest(2, ms)))
    return (max(ms) if ms else 0) + 1
  def treeDiameter(self, edges: List[List[int]]) -> int:
    # construct graph
    self.graph = defaultdict(set)
    for u, v in edges:
      self.graph[u].add(v)
      self.graph[v].add(u)
    # dfs
    self.diameter, self.visited = 0, set([0])
    self.recursive(0)
    return self.diameter

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,1],[0,2]],
    [[0,1],[1,2],[2,3],[1,4],[4,5]],
  ]
  rslts = [solver.treeDiameter(edges) for edges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
