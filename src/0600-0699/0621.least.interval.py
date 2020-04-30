from typing import List
from  collections import Counter

import heapq

class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    q = [-m for m in Counter(tasks).values()]
    heapq.heapify(q)
    idles = 0
    if q:
      m = -heapq.heappop(q)
      idles = (m - 1) * n
    print(m, idles)
    while q and idles > 0:
      p = -heapq.heappop(q)
      idles -= min(p, m - 1)
    return len(tasks) + max(idles, 0)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # (["A","A","A","B","B","B"], 2),
    (["A","A","A","A","A","A","B","C","D","E","F","G"], 2)
  ]
  rslts = [solver.leastInterval(tasks, n) for tasks, n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
