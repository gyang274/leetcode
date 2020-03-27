from typing import List
from collections import defaultdict

class Solution:
  def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    """A[i] + B[j] + C[k] + D[l] = 0 => A[i] + B[j] = - (C[k] + D[l])
    """
    dAB = defaultdict(lambda: 0)
    for x in A:
      for y in B:
        dAB[x + y] += 1
    dCD = defaultdict(lambda: 0)
    for x in C:
      for y in D:
        dCD[x + y] += 1
    count = 0
    for d in dAB:
      count += dAB[d] * dCD[-d]
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1, 2], [-2, -1], [-1, 2], [0, 2]),
  ]
  rslts = [solver.fourSumCount(A, B, C, D) for A, B, C, D in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")