from typing import List
from collections import defaultdict

import heapq

class Solution:
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    # a-star search
    graph = defaultdict(set)
    for (u, v), p in zip(edges, succProb):
      graph[u].add((v, p))
      graph[v].add((u, p))
    # init
    q, seen = [(-p, v) for v, p in graph[start]], {start}
    heapq.heapify(q)
    while q:
      _p, u = heapq.heappop(q)
      if u == end:
        return -_p
      if u not in seen:
        seen.add(u)
        for v, p in graph[u]:
          heapq.heappush(q, (_p * p, v))
    return 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, [[0,1]], [0.5], 0, 2),
    (3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2),
    (3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2),
    (5, [[2,3],[1,2],[3,4],[1,3],[1,4],[0,1],[2,4],[0,4],[0,2]], [0.06,0.26,0.49,0.25,0.2,0.64,0.23,0.21,0.77], 0, 3),
  ]
  rslts = [solver.maxProbability(n, edges, succProb, start, end) for n, edges, succProb, start, end in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
