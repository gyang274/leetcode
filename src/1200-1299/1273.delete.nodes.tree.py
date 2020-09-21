from typing import List
from collections import defaultdict
from functools import reduce

class Solution:
  def __init__(self):
    self.r = lambda x, y: (x[0] + y[0], x[1] + y[1])
  def recursive(self, node):
    xs = [self.recursive(v) for v in self.graph[node]]
    x, n = reduce(self.r, xs + [(self.value[node], 1)])
    return (x, n) if x else (0, 0)
  def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
    # constuct graph
    self.graph = defaultdict(set)
    for v, u in enumerate(parent):
      if not u == -1:
        self.graph[u].add(v)
    self.value = value
    # recursive
    return self.recursive(0)[1]

class Solution:
  def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
    # O(N), one pass, require condition/assumption: parernt[i] < i for all i > 0, and sum(values) != 0.
    ans = [1] * nodes
    for i in range(nodes - 1, 0, -1):
      value[parent[i]] += value[i]
      ans[parent[i]] += ans[i] if value[i] else 0
    return ans[0] if value[0] else 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (7, [-1,0,0,1,2,2,2], [1,-2,4,0,-2,-1,-1]),
  ]
  rslts = [solver.deleteTreeNodes(nodes, parent, value) for nodes, parent, value in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
