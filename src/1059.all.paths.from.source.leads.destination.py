from typing import List
from collections import defaultdict

class Solution:
  def dfs(self, path, node):
    # reach destination
    if node not in self.graph:
      return node == self.destination
    # reach inifinte loop
    if node in path:
      return False
    path.add(node)
    for nuxt in self.graph[node]:
      if not self.dfs(path.copy(), nuxt):
        return False
    return True
  def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    self.graph = defaultdict(set)
    for u, v in edges:
      self.graph[u].add(v)
    self.destination = destination
    return self.dfs(set(), source)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, [[0,1],[1,1]], 0, 1),
    (3, [[0,1],[0,2]], 0, 2),
    (3, [[0,1],[1,1],[1,2]], 0, 2),
    (4, [[0,1],[0,3],[1,2],[2,1]], 0, 3),
    (4, [[0,1],[0,2],[1,3],[2,3]], 0, 3),
  ]
  rslts = [solver.leadsToDestination(n, edges, source, destination) for n, edges, source, destination in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
