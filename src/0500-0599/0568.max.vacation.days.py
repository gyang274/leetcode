from typing import List

import itertools

class Solution:
  def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
    """O(NKlogNK) as shortest path.
      s - (n cities) - (n cities) - .. - (n cities) - t
          ---- repeat K of (n cities)
      connect s to 1st n cities, connect n cities in different week w.r.t flights, connects last n cities to t,
      and max value can be derived from negative shortest path. However, contruct the graph requires O(NNK).
    
      O(NNK) using dynamic programming.
    """
    n, k = len(days), len(days[0])
    # dp[i]: max vacation days by staying at i-th city at last day
    dp = [-1] * n
    dp[0] = 0
    # src: s[i] = 1/0, i-th city available to stay at current day or not
    src = [0] * n
    src[0] = 1
    # flight transpose: all src -> one dst
    for i in range(n):
      flights[i][i] = 1
    ft = list(zip(*flights))
    for j in range(k):
      # move to next day
      qb = dp.copy()
      for i in range(n):
        isrc = [(s & t) for s, t in zip(src, ft[i])]
        iprv = list(itertools.compress(dp, isrc))
        # print(f"days {j=}, city {i=}, from {isrc=}, with previous vacation {iprv=}")
        if iprv:
          qb[i] = max(max(iprv), 0) + days[i][j]
      dp = qb
      # print(f"update {dp=}")
      src = [1 if dp[i] > -1 else 0 for i in range(n)]
      # print(f"update {src=}")
    return max(dp)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,1,1],[1,0,1],[1,1,0]], [[1,3,1],[6,0,3],[3,3,3]]),
    ([[0,0,0],[0,0,0],[0,0,0]], [[1,1,1],[7,7,7],[7,7,7]]),
    ([[0,1,1],[1,0,1],[1,1,0]], [[7,0,0],[0,7,0],[0,0,7]]),
    ([[0,1,0],[0,0,0],[0,0,0]], [[0,0,7],[2,7,7],[7,7,7]]),
  ]
  rslts = [solver.maxVacationDays(flights, days) for flights, days in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
