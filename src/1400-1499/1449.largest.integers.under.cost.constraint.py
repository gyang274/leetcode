from typing import List
from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, k):
    if k == 0:
      return ''
    ans = []
    for x in self.d:
      if x <= k:
        r = self.recursive(k - x)
        if r != '0':
          ans.append(self.d[x] + r)
    return str(max(map(int, ans))) if ans else '0'
  def largestNumber(self, cost: List[int], target: int) -> str:
    # self.d: cost -> digit, same cost always prefer larger digit
    self.d = {}
    for i, x in enumerate(cost):
      self.d[x] = str(i + 1)
    self.recursive.cache_clear()
    return self.recursive(target)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([4,3,2,5,6,7,2,5,5], 9),
    ([2,4,6,2,4,6,4,4,4], 5),
    ([7,6,5,5,5,6,8,7,8], 12),
  ]
  rslts = [solver.largestNumber(cost, target) for cost, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
