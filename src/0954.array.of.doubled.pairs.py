from typing import List
from collections import Counter

class Solution:
  def canReorderDoubled(self, A: List[int]) -> bool:
    A.sort()
    d = Counter(A)
    for x in A:
      if d[x] > 0:
        if x == 0:
          if d[x] & 1:
            return False
        elif x > 0:
          if d[x * 2] >= d[x]:
            d[x * 2] -= d[x]
          else:
            return False
        else:
          if ((x & 1) ^ 1) and d[x // 2] >= d[x]:
            d[x // 2] -= d[x]
          else:
            return False
        d[x] = 0
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,1,2,4],
    [3,2,4,8],
    [4,-2,2,-4],
    [1,2,4,16,8,4],
  ]
  rslts = [solver.canReorderDoubled(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
