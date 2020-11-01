from typing import List
from collections import defaultdict, deque

import heapq

class Solution:
  def avoidFlood(self, rains: List[int]) -> List[int]:
    # TC: O(NlogN), SC: O(N).
    n = len(rains)
    d = defaultdict(deque)
    for i, x in enumerate(rains):
      if x > 0:
        d[x].append(i)
    ans, q, s = [1] * n, [], set()
    for i, x in enumerate(rains):
      if x > 0:
        if x in s:
          return []
        ans[i] = -1
        # lake x pop index i
        d[x].popleft()
        # if will rain on lake x in the future
        if d[x]:
          s.add(x)
          heapq.heappush(q, (d[x][0], x))
      else:
        if q:
          j, y = heapq.heappop(q)
          if j > i:
            ans[i] = y
            s.remove(y)
          else:
            return []
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,0,1,4],
    [1,0,1,1,0,0],
    [2,0,3,0,2,3],
    [2,0,3,0,3,2],
  ]
  rslts = [solver.avoidFlood(rains) for rains in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
