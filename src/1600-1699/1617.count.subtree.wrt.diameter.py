from typing import List
from collections import defaultdict

import math

class Solution:
  def bfs(self, nodes):
    # root
    maxlevel = 0
    for i in range(self.n):
      if (1 << i) & nodes:
        seen, visit, level = 1 << i, 0, -1
        while seen > visit:
          level += 1
          bound = visit ^ seen
          visit = seen
          while bound:
            # index of rightmost bit 1, 0-indexed.
            i = int(math.log2(bound & -bound))
            # explore i-th node connections within subtree
            seen |= (self.d[i] & nodes)
            # set it to 0
            bound ^= 1 << i
        if seen < nodes:
          return 0
        maxlevel = max(maxlevel, level)
    return maxlevel
  def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
    self.n = n
    # TC: O(N^2 * 2^N), bfs x bitmask, SC: O(N)
    self.d = defaultdict(lambda: 0)
    for u, v in edges:
      self.d[u - 1] |= 1 << (v - 1)
      self.d[v - 1] |= 1 << (u - 1)
    # print(self.d)
    self.count = [0] * n
    # only 1 vertex..
    for i in range(1, 1 << n):
      self.count[self.bfs(i)] += 1
    return self.count[1:]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, [[1,2]]),
    (3, [[1,2],[2,3]]),
    (4, [[1,2],[2,3],[2,4]]),
    (4, [[1,3],[1,4],[2,3]]),
  ]
  rslts = [solver.countSubgraphsForEachDiameter(n, edges) for n, edges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
