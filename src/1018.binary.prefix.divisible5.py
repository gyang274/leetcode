from typing import List
from itertools import accumulate

class Solution:
  def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    n = len(A)
    r = [0] * n
    r[0] = A[0]
    for i in range(1, n):
      r[i] = ((r[i - 1] << 1) + A[i]) % 5
    return list(map(lambda x: x == 0, r))

class Solution:
  def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    return list(map(lambda x: x == 0, accumulate(A, lambda x, y: ((x << 1) | y) % 5)))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0,0,1,0,1,1,0,0],
  ]
  rslts = [solver.prefixesDivBy5(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
