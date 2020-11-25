from typing import List

import heapq

class Solution:
  def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
    # TC: O(NlogK), n: num of request, k: num of servers
    n = len(arrival)
    # q: priority queue of servers busy running some requests, queue with ende time
    # qa, qb: priority queue of servers index after and before current round robin index
    # rs: num of request handled by each server
    q, qa, qb, rs = [], [], list(range(k)), [0] * k
    for i in range(n):
      # default server index under roundrobin schedule
      r = i % k
      if r == 0:
        qa, qb = qb, []
      # release servers completed previous requests at this moment
      while q and q[0][0] <= arrival[i]:
        _, s = heapq.heappop(q)
        if s >= r:
          heapq.heappush(qa, s)
        else:
          heapq.heappush(qb, s)
      # schedule this request to next idle server
      qc = qa if qa else qb
      if qc:
        s = heapq.heappop(qc)
        heapq.heappush(q, (arrival[i] + load[i], s))
        rs[s] += 1
    m = max(rs)
    return [i for i in range(k) if rs[i] == m]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, [1], [1]),
    (3, [1,2,3], [2,3,1]),
    (3, [1,2,3,4], [1,2,1,2]),
    (3, [1,2,3,4,5], [5,2,3,3,3]),
    (3, [1,2,3,4,8,9,10], [5,2,10,3,1,2,2]),
  ]
  rslts = [solver.busiestServers(k, arrival, load) for k, arrival, load in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
