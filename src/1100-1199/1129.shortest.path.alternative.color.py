from typing import List
from collections import defaultdict

import heapq

class Solution:
  def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
    # e: (node, color) -> next, color = 0 if red else 1
    e = defaultdict(set)
    for u, v in red_edges:
      e[(u, 0)].add(v)
    for u, v in blue_edges:
      e[(u, 1)].add(v)
    # q: dist, node, color for next
    q, d, seen = [(0, 0, 0), (0, 0, 1)], {0: 0}, set()
    while q and len(d) < n:
      dist, node, color = heapq.heappop(q)
      if node not in d:
        d[node] = dist
      if (node, color) not in seen:
        for nuxt in e[(node, color)]:
          heapq.heappush(q, (dist + 1, nuxt, color ^ 1))
        seen.add((node, color))
    return [d.get(i, -1) for i in range(n)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, [[0,1]], [[1,2]]),
    (3, [[0,1]], [[2,1]]),
    (3, [[1,0]], [[2,1]]),
    (3, [[0,1],[1,2]], []),
    (3, [[0,1],[0,2]], [[1,0]]),
  ]
  rslts = [solver.shortestAlternatingPaths(n, red_edges, blue_edges) for n, red_edges, blue_edges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
