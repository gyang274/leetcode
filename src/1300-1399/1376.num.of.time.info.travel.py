from typing import List
from collections import defaultdict

class Solution:
  def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    # bfs
    # built tree
    d = defaultdict(lambda: [set(), 0])
    for v, u in enumerate(manager):
      if u >= 0:
        d[u][0].add(v)
        d[u][1] = informTime[u]
    # info travel
    q, m = [(headID, 0)], 0
    for u, x in q:
      y = x + d[u][1]
      for v in d[u][0]:
        q.append((v, y))
        m = max(m, y)
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 0, [-1], [0]),
    (4, 2, [2,2,-1,2], [0,0,1,0]),
    (7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1]),
    (15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,2,3,5,8,7,4,0,0,0,0,0,0,0,0]),
  ]
  rslts = [solver.numOfMinutes(n, headID, manager, informTime) for n, headID, manager, informTime in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
