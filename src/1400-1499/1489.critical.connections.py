from typing import List
from collections import defaultdict

import heapq

class Solution:
  def minCost(self, n, graph, cost, nodes, edges) -> int:
    # Prim's Minimum Spanning Tree Algorithm, TC: O(ElogV), SC: O(E)
    #  keep adding the edge with minimum weight from all edges over visited nodes
    # Args:
    #  graph: u -> {(w, v), ..}, where u, v are nodes, w is weight of (u, v).
    #  cost, nodes, edges: initial cost, and nodes and edges must be included.
    # init
    r = list(nodes)[0]
    heapq.heapify(edges)
    # main
    while edges:
      # adding the edge with minimum weight from all edges over visited node
      w, u = 0, r
      while (u in nodes) and edges:
        w, u = heapq.heappop(edges)
      if u not in nodes:
        cost += w
        nodes.add(u)
        for w, v in graph[u]:
          heapq.heappush(edges, (w, v))
    return cost if len(nodes) == n else float('inf')
  def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
      # build graphs
      graph = defaultdict(set)
      for u, v, w in edges:
        graph[u].add((w, v))
        graph[v].add((w, u))
      # mst over complete graph
      xmin = self.minCost(n, graph, 0, {0}, list(graph[0]))
      # critical and pseudo-critical edges
      ce, pe = [], []
      for i, (u, v, w) in enumerate(edges):
        # ce: iff delete (u, v, w) leads mst cost increase
        graph[u].remove((w, v))
        graph[v].remove((w, u))
        if self.minCost(n, graph, 0, {0}, list(graph[0])) > xmin:
          ce.append(i)
        else:
          # pe: iff add (u, v, w) into spanning tree not lead cost increase
          if self.minCost(n, graph, w, set([u, v]), list(graph[u] | graph[v])) == xmin:
            pe.append(i)
        graph[u].add((w, v))
        graph[v].add((w, u))
      return [ce, pe]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]),
    (5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]),
  ]
  rslts = [solver.findCriticalAndPseudoCriticalEdges(n, edges) for n, edges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
