from typing import List
from collections import defaultdict

import heapq

class Solution:
  def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
    # graph: w as weight.
    graph = defaultdict(dict)
    for u, v, w in edges:
      graph[u][v] = w
      graph[v][u] = w
    # dijkstra algorithm, modified.
    queue, node, seen, count = [(0, 0)], {0}, {}, 0
    while queue:
      # node, move
      m, u = heapq.heappop(queue)
      for v in graph[u]:
        if (u, v) not in seen:
          if m + graph[u][v] < M:
            node.add(v)
            seen[(u, v)] = graph[u][v]
            seen[(v, u)] = graph[v][u]
            heapq.heappush(queue, (m + graph[u][v] + 1, v))
          else:
            seen[(u, v)] = M - m
            if (v, u) in seen:
              seen[(u, v)] = min(seen[(u, v)], graph[u][v] - seen[(v, u)])
          count += seen[(u, v)]
    return count + len(node)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,1,9],[0,2,1],[1,2,2]], 6, 3),
    ([[0,1,4],[1,2,6],[0,2,8],[1,3,1]], 10, 4),
    ([[0,1,9],[0,2,1],[0,3,2],[1,2,2],[1,3,4],[2,3,2]], 7, 4),
  ]
  rslts = [solver.reachableNodes(edges, M, N) for edges, M, N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
