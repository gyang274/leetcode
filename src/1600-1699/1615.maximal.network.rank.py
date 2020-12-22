from typing import List
from collections import defaultdict

class Solution:
  def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
    r = set()
    d = defaultdict(lambda: 0)
    for u, v in roads:
      d[u] += 1
      d[v] += 1
      r.add((min(u, v), max(u, v)))
    m = 0
    for i in range(n):
      for j in range(i + 1, n):
        m = max(m, d[i] + d[j] - (1 if (i, j) in r else 0))
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [[0,1],[0,3],[1,2],[1,3]]),
    (4, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]),
    (8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]),
  ]
  rslts = [solver.maximalNetworkRank(n, roads) for n, roads in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
