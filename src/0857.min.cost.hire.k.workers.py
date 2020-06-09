from typing import List

import heapq

class Solution:
  def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
    # min sum(Qi) x max(WQ_i), i \in I, |I| = K, Q: quality, WQ: wage/quality
    # so sorted by wage/quality ratio, make max(WQ_i) increase monotonically, 
    # keep a queue of size K that minimize sum of quality under the WQ bound.
    worker = sorted([(w / q, -q) for q, w in zip(quality, wage)])
    # init queue with K workers
    queue = [q for _, q in worker[:K]]
    heapq.heapify(queue)
    # main
    quals = sum(-q for q in queue)
    costs = worker[K - 1][0] * quals
    for i in range(K, len(worker)):
      # higher WQ, w/ possible lower sum(Q)
      if queue[0] < worker[i][1]:
        quals += queue[0] - worker[i][1]
        heapq.heappushpop(queue, worker[i][1])
        costs = min(costs, worker[i][0] * quals)
    return costs

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([5,10,20], [30,70,50], 2),
    ([5,10,20], [30,10,50], 2),
    ([1,1,3,10,10], [7,8,4,2,2], 3),
    ([32,43,66,9,94,57,25,44,99,19], [187,366,117,363,121,494,348,382,385,262], 4),
  ]
  rslts = [solver.mincostToHireWorkers(quality, wage, K) for quality, wage, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
