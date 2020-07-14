from typing import List

import heapq

class Solution:
  def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    n = len(days)
    # d: day next travel on day x, this mitigate the O(logN) search later.
    d, j = {}, 0
    for i in range(396):
      if j < n:
        if i < days[j]:
          d[i] = days[j]
        else:
          j += 1
          if j < n:
            d[i] = days[j]
          else:
            d[i] = -1
      else:
        d[i] = -1
    # q: queue of (cost, day-next-travel)
    q, s = [(0, d[0])], {}
    while q:
      c, k = heapq.heappop(q)
      if k == -1:
        return c
      # buy 1-day ticket
      if d[k] not in s or s[d[k]] > c + costs[0]:
        s[d[k]] = c + costs[0]
        heapq.heappush(q, (c + costs[0], d[k]))
      # buy 7-day ticket
      if d[k + 6] not in s or s[d[k + 6]] > c + costs[1]:
        s[d[k + 6]] = c + costs[1]
        heapq.heappush(q, (c + costs[1], d[k + 6]))
      # buy 29-day ticket
      if d[k + 29] not in s or s[d[k + 29]] > c + costs[2]:
        s[d[k + 29]] = c + costs[2]
        heapq.heappush(q, (c + costs[2], d[k + 29]))
    return -1

from functools import lru_cache

class Solution:
  def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    """dynamic programming: dp(i) = min(dp(i + duration) + cost for (cost, duration) in zip(costs, [1,7,30]))
    """
    days = set(days)

    @lru_cache
    def dp(i):
      if i > 365:
        return 0
      elif i in days:
        return min(dp(i + duration) + cost for cost, duration in zip(costs, [1, 7, 30]))
      else:
        return dp(i + 1)
    
    return dp(1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,4,6,7,8,20], [2,7,15]),
    ([1,4,6,7,8,365], [2,7,15]),
    ([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]),
  ]
  rslts = [solver.mincostTickets(days, costs) for days, costs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
