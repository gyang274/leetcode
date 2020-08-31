from typing import List
from collections import defaultdict

import bisect

class Solution:
  def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
    # d: color -> indexes
    d = defaultdict(lambda: [float('-inf')])
    for i, x in enumerate(colors):
      d[x].append(i)
    for x in [1,2,3]:
      d[x].append(float('inf'))
    # binary search
    ans = [None] * len(queries)
    for i, (j, x) in enumerate(queries):
      k = bisect.bisect(d[x], j)
      ans[i] = min(d[x][k] - j, j - d[x][k - 1])
    return [z if z < float('inf') else -1 for z in ans]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2], [[0,3]]),
    ([1,1,2,1,3,2,2,3,3], [[1,3],[2,2],[6,1]]),
  ]
  rslts = [solver.shortestDistanceColor(colors, queries) for colors, queries in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
