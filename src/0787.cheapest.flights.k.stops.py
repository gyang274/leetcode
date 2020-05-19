from typing import List
from collections import defaultdict

class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    # d: src -> (dst, price)
    d = defaultdict(list)
    for s, t, p in flights:
      d[s].append((t, p))
    # bfs modified w.r.t K
    srcs, seen = [(src, 0)], {src: 0}
    stop, xmin = -1, float('inf')
    while stop < K and srcs:
      snxt = []
      for s, p in srcs:
        for t, q in d[s]:
          if t == dst:
            xmin = min(xmin, p + q)
          if t not in seen or seen[t] > p + q:
            seen[t] = p + q
            snxt.append((t, p + q))
      srcs = snxt
      stop += 1
    return xmin if xmin < float('inf') else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0),
    (3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 2),
  ]
  rslts = [solver.findCheapestPrice(n, flights, src, dst, K) for n, flights, src, dst, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
