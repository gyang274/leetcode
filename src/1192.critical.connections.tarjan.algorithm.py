from typing import List
from collections import defaultdict

class Solution:
  def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    # Tarjan's algorithm: https://cp-algorithms.com/graph/bridge-searching.html#toc-tgt-1
    if not connections:
      return []
    # build graph
    graph = defaultdict(set)
    for u, v in connections:
      graph[u].add(v)
      graph[v].add(u)
    # lowest: lowest level reached this node through dfs
    # cc: critical connections, e.g. bridges
    rlowest, visited, cc = {}, {0}, []
    def dfs(node, parent, level):
      # rlowest[v]: lowest level this node being reached
      rlowest[node] = level
      # vlowest: lowest level this node can reach via dfs
      vlowest = level
      for nuxt in graph[node]:
        if nuxt not in visited:
          visited.add(nuxt)
          ulowest = dfs(nuxt, node, level + 1)
          if ulowest > level:
            # no way back, no cycle back.
            cc.append((node, nuxt))
          vlowest = min(vlowest, ulowest)
        elif nuxt != parent:
          vlowest = min(vlowest, rlowest[nuxt])
      return vlowest        
    dfs(0, None, 0)
    return cc

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [[0,1],[1,2],[2,0],[1,3]]),
  ]
  rslts = [solver.criticalConnections(n, connections) for n, connections in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
