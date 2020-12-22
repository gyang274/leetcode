from typing import List

import heapq

class Solution:
  def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
    # bfs
    if x == 0:
      return 0
    seen, q = set([0] + forbidden), [(0, 0, -1)]
    bound = max(x, max(seen)) + a + b
    while q:
      # d: previous move direction, 1 previous one moved forward, -1 previous one moved backward
      m, p, d = heapq.heappop(q)
      if p + a == x:
        return m + 1
      if d > 0 and p - b == x:
        return m + 1
      if p + a <= bound and p + a not in seen:
        seen.add(p + a)
        heapq.heappush(q, (m + 1, p + a, 1))
      if d > 0 and p - b >= 0 and p - b not in seen:
        seen.add(p - b)
        heapq.heappush(q, (m + 1, p - b, -1))
    return -1
