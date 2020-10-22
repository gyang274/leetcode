from typing import List
from functools import lru_cache

import math

class Solution:
  @lru_cache(None)
  def simplifiedFractions(self, n: int) -> List[str]:
    return [str(x) + "/" + str(y) for y in range(2, n + 1) for x in range(1, y) if math.gcd(x, y) == 1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, # 23, 42, 85,
  ]
  rslts = [solver.simplifiedFractions(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
