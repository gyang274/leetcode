from typing import List
from collections import defaultdict

class Solution:
  def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
    d = defaultdict(set)
    for u, v in edges:
      d[u].add(v)
      d[v].add(u)
    q, seen = {1: 1.0}, set([1])
    for _ in range(t):
      r = defaultdict(lambda: 0)
      for u in q:
        vs = d[u] - seen
        if vs:
          for v in vs:
            r[v] += q[u] / len(vs)
          seen |= d[u]
        else:
          r[u] = q[u]
      if q == r:
        break
      q = r
    return q[target] if target in q else 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4),
    (7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 4, 2),
    (7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1, 7),
    (7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 4, 7),
    (7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 7, 4),
    (7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 7, 7),
  ]
  rslts = [solver.frogPosition(n, edges, t, target) for n, edges, t, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
