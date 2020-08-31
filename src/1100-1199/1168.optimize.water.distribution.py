from typing import List
from collections import defaultdict

import heapq

class Solution:
  def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
    # graph, minimum spanning tree, O(MlogN), M = edges, N = nodes, prim's algorithm.
    # create a sentinel node as water source, so wells[i] is the cost of building pipe source -> house[i],
    # and now all costs are associated to edge, problem is equivalent to find MST connect all nodes.
    graph = defaultdict(list)
    graph[0] = [(x, i + 1) for i, x in enumerate(wells)]
    for i, j, x in pipes:
      graph[i].append((x, j))
      graph[j].append((x, i))
    # heapify
    for i in range(n):
      heapq.heapify(graph[i])
    # prim's algorithm
    # keep adding the edge with minimum weight from all edges over visited nodes
    # init with node 0
    cost, seen, edge = 0, {0}, graph[0]
    while len(seen) < n + 1:
      # adding the edge with minimum weight from all edges over visited node
      w, node = 0, 0
      while node in seen:
        w, node = heapq.heappop(edge)
      cost += w
      seen.add(node)
      for x, i in graph[node]:
        heapq.heappush(edge, (x, i))
    return cost

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, [1,2,2], [[1,2,1],[2,3,1]]),
  ]
  rslts = [solver.minCostToSupplyWater(n, wells, pipes) for n, wells, pipes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
