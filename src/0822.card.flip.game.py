from typing import List

class Solution:
  def flipgame(self, fronts: List[int], backs: List[int]) -> int:
    banned = set(x for x, y in zip(fronts, backs) if x == y)
    # min of not banned
    xmin = float('inf')
    for x, y in zip(fronts, backs):
      if not x == y:
        s, t = min(x, y), max(x, y)
        if s not in banned:
          xmin = min(xmin, s)
        elif t not in banned:
          xmin = min(xmin, t)
    return 0 if xmin == float('inf') else xmin

import itertools

class Solution:
  def flipgame(self, fronts: List[int], backs: List[int]) -> int:
    same = {x for x, y in zip(fronts, backs) if x == y}
    ans = 214748367
    for x in itertools.chain(fronts, backs):
      if x not in same:
        ans = min(ans, x)
    return ans % 214748367

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,4,4,7], [1,3,4,1,3]),
    ([2,3,1,1,4], [3,2,1,5,4]),
    ([2,1,1,2,2], [2,2,1,2,1]),
  ]
  rslts = [solver.flipgame(fronts, backs) for fronts, backs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
