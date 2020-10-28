from typing import List
from functools import lru_cache
from itertools import accumulate

import heapq

class Solution:
  @lru_cache(None)
  def recursive(self, i, j, s):
    # cost of paint houses[i:j] with s segments of color
    if s == 1:
      return heapq.nsmallest(2, ((self.cost[u][j] - self.cost[u][i], u, u) for u in range(self.n)))
    q = []
    for l in range(1, s):
      r = s - l
      for k in range(i + l, j - r + 1):
        L = self.recursive(i, k, l)
        R = self.recursive(k, j, r)
        print(i, j, k, L, R)
        # cost and color on leftmost/rightmost
        for x, xl, xr in L:
          for y, yl, yr in R:
            if xr == yl:
              continue
            q.append((x + y, xl, yr))
    heapq.heapify(q)
    print(i, j, s, q)
    # make sure at least one alternative color on left and right
    ans = [heapq.heappop(q)]
    al, ar = False, False
    while q:
      z, zl, zr = heapq.heappop(q)
      if zl == ans[0][1] and zr == ans[0][2]:
        continue
      if (not al and zl != ans[0][1]) or (not ar and zr != ans[0][2]):
        ans.append((z, zl, zr))
        al = zl != ans[0][1]
        ar = zr != ans[0][2]
      if al and ar:
        break
    return ans
  def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    # NOTE: this solution assumes painted houses can be repainted..
    # divide and conquer
    self.m, self.n, self.cost = m, n, list(map(list, zip(*cost)))
    print(self.cost)
    for j, i in enumerate(houses):
      if i > 0:
        self.cost[i - 1][j] = 0
    # prefix sum of cost over houses on each color
    self.cost = list(map(lambda x: list(accumulate(x, initial=0)), self.cost))
    print(self.cost)
    # divide and conquer
    self.recursive.cache_clear()
    return self.recursive(0, m, target)[0][0]

class Solution:
  def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    # TC: O(MNNT), SC: (NT)
    # dp: (n-color, t-blocks): min-cost
    dp0, dp1 = {(0, 0): 0}, {}
    for i, k in enumerate(houses):
      # assume painted houses can NOT be repainted..
      for ik in ([k] if k > 0 else range(1, n + 1)):
        # previous color and blocks
        for pk, pb in dp0:
          bb = pb + (ik != pk)
          if bb > target:
            continue
          dp1[ik, bb] = min(dp1.get((ik, bb), float('inf')), dp0[pk, pb] + (0 if k > 0 else cost[i][ik - 1]))
      dp0, dp1 = dp1, {}
    return min([dp0[k, b] for k, b in dp0 if b == target] or [-1])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([3,1,2,3], [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 4, 3, 3),
    ([0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3),
    ([0,2,1,2,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3),
    ([0,0,0,0,0], [[1,10],[10,1],[1,10],[10,1],[1,10]], 5, 2, 5),
  ]
  rslts = [solver.minCost(houses, cost, m, n, target) for houses, cost, m, n, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
