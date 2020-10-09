from typing import List

import heapq

class Solution:
  def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    """TC: O(NlogN), Q0857.
    """
    M = 10 ** 9 + 7
    # max sum(S) * min(E), i in I, |I| = k
    # sort by the efficiency descending so min(E) descrease monotonically,
    # keep a queue of size k, such that maximize the sum(S) under E bound.
    worker = sorted([(e, s) for e, s in zip(efficiency, speed)], reverse=True)
    # init
    queue, s, p = [], 0, 0
    for i in range(n):
      # lower E, w/ possible higher S
      heapq.heappush(queue, worker[i][1])
      s += worker[i][1]
      if len(queue) > k:
        s -= heapq.heappop(queue)
      p = max(p, worker[i][0] * s)
    return p % M

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, [2,8,2], [2,7,1], 2),
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2),
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3),
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4),
  ]
  rslts = [solver.maxPerformance(n, speed, efficiency, k) for n, speed, efficiency, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
