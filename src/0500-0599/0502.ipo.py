from typing import List

class Solution:
  def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
    """modified knapsack.
    """
    cp = sorted([(c, p) for c, p in zip(Capital, Profits)], key=lambda x: (x[0], -x[1]))
    dp = [W] * (k + 1)
    for c, p in cp:
      # binary search, i s.t., dp[i] >= c, since dp must be non-decreasing
      l, r = 0, k + 1
      while l < r:
        m = l + (r - l) // 2
        if dp[m] >= c:
          r = m
        else:
          l = m + 1
      for i in range(k - 1, l - 1, -1):
        dp[i + 1] = max(dp[i + 1], dp[i] + p)
    return dp[k]

class Solution:
  def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
    """greedy approach.
    """
    cp = sorted([(c, p) for c, p in zip(Capital, Profits)], key=lambda x: (x[0], -x[1]))
    cs = [c for c, p in cp]
    ps = [p for c, p in cp]
    # binary search over project, always go with maximum profit with affordable capital
    w = W
    for i in range(k):
      l, r = 0, len(cs)
      while l < r:
        m = l + (r - l) // 2
        if w < cs[m]:
          r = m
        else:
          l = m + 1
      if l > 0:
        imax = ps.index(max(ps[:l]))
        w += ps[imax]
        cs = cs[:imax] + cs[(imax + 1):]
        ps = ps[:imax] + ps[(imax + 1):]
      else:
        break
    return w

import heapq

class Solution:
  def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
    """greedy approach + priority queue.
    """
    # w: capital available at eath time t
    w = W
    if W >= max(Capital):
      # trival case when all projects are possible at the very beginning
      profits = [-p for p in Profits]
      heapq.heapify(profits)
      for _ in range(k):
        w -= heapq.heappop(profits)
    else:
      # priority queue on unrealized projects sorted by profits in descending order
      unrealized = []
      # priority queue on impossible projects sorted by captial in ascending order
      impossible = list(zip(Capital, Profits))
      # heapq.heapify: list to priority queue, in-place, linear time.
      heapq.heapify(impossible)
      for _ in range(k):
        while impossible and w >= impossible[0][0]:
          heapq.heappush(unrealized, -heapq.heappop(impossible)[1])
        if unrealized:
          w -= heapq.heappop(unrealized)
        else:
          break
    return w

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 0, [1,2,3], [0,1,1]),
    (2, 0, [1,2,2], [0,0,1]),
  ]
  rslts = [solver.findMaximizedCapital(k, W, Profits, Capital) for k, W, Profits, Capital in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
