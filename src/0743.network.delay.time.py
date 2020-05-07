from typing import List
from collections import defaultdict

import heapq

class Solution:
  def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
    """dijkstra algorithm, O(E + VlogV).
    """
    # define graph G(E, V)
    graph = defaultdict(set)
    for u, v, w in times:
      graph[u].add((v, w))
    # initialize dijkstra algorithm
    dist, queue = {}, [(0, K)]
    while queue:
      d, u = heapq.heappop(queue)
      if u not in dist:
        dist[u] = d
        for v, w in graph[u]:
          heapq.heappush(queue, (d + w, v))
    return -1 if len(dist) < N else max(dist.values())

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[2,1,1],[2,3,1],[3,4,1]], 4, 2),
  ]
  rslts = [solver.networkDelayTime(times, N, K) for times, N, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
