from typing import List
from collections import defaultdict

import heapq

class Solution:
  def minimumCost(self, N: int, connections: List[List[int]]) -> int:
    # graph, minimum spanning tree, O(MlogN), M = edges, N = nodes, prim's algorithm.
    graph = defaultdict(list)
    for i, j, x in connections:
      graph[i].append((x, j))
      graph[j].append((x, i))
    # heapify
    for i in range(1, N + 1):
      heapq.heapify(graph[i])
    # prim's algorithm
    # keep adding the edge with minimum weight from all edges over visited nodes
    # init with node 1
    cost, seen, edge = 0, {1}, graph[1]
    while edge and len(seen) < N:
      # adding the edge with minimum weight from all edges over visited node
      x, node = 0, 1
      while (node in seen) and edge:
        x, node = heapq.heappop(edge)
      if node not in seen:
        cost += x
        seen.add(node)
        for x, i in graph[node]:
          heapq.heappush(edge, (x, i))
    return cost if len(seen) == N else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [[1,2,3],[3,4,4]]),
    (3, [[1,2,5],[1,3,6],[2,3,1]]),
    (7, [[2,1,4697],[3,2,93142],[4,3,36786],[5,4,65078],[6,5,87350]]),
  ]
  rslts = [solver.minimumCost(N, connections) for N, connections in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
