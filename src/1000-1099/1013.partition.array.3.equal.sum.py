from typing import List
from collections import defaultdict
from itertools import accumulate

class Solution:
  def canThreePartsEqualSum(self, A: List[int]) -> bool:
    A, d = list(accumulate(A)), defaultdict(list)
    for i, x in enumerate(A):
      d[x].append(i)
    x, y, z = A[-1] // 3, A[-1] * 2 // 3, A[-1]
    if z == 0:
      return len(d[0]) >= 3
    if z % 3:
      return False
    return x in d and y in d and d[x][0] < d[y][-1]

class Solution:
  def canThreePartsEqualSum(self, A: List[int]) -> bool:
    # one pass
    s = sum(A)
    if s % 3:
      return False
    s //= 3
    r, count = 0, 0
    for x in A[:-1]:
      r += x
      if r == s:
        count += 1
        r = 0
        if count == 2:
          return True
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [4,-2,4],
    [1,-1,1,-1],
    [0,2,1,-6,6,-7,9,1,2,0,1],
    [0,2,1,-6,6,7,9,-1,2,0,1],
  ]
  rslts = [solver.canThreePartsEqualSum(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
