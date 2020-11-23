from typing import List
from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, i, mask):
    # i: index of row, mask: bitmask of cols taken
    ans = float('inf') if i < self.m else 0
    if i < self.m:
      for j in range(self.n):
        ans = min(ans, self.cost[i][j] + self.recursive(i + 1, mask | (1 << j)))
    else:
      for j in range(self.n):
        if mask & (1 << j) == 0:
          ans += self.mincolcost[j]
    return ans
  def connectTwoGroups(self, cost: List[List[int]]) -> int:
    self.cost = cost
    self.m, self.n = len(cost), len(cost[0])
    self.mincolcost = list(map(min, zip(*cost)))
    self.recursive.cache_clear()
    return self.recursive(0, 0)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[15,96],[36,2]],
    [[1,3,5],[4,1,1],[1,5,3]],
    [[2,5,1],[3,4,7],[8,1,2],[6,2,4],[3,8,8]],
    [[93,56,92],[53,44,18],[86,44,69],[54,60,30]],
  ]
  rslts = [solver.connectTwoGroups(cost) for cost in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
