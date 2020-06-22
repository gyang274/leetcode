from typing import List
from collections import Counter

import itertools

class Solution:
  def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
    n = len(A)
    a = [(i, j) for i in range(n) for j in range(n) if A[i][j] == 1]
    b = [(i, j) for i in range(n) for j in range(n) if B[i][j] == 1]
    m = [(ai - bi, aj - bj) for (ai, aj), (bi, bj) in itertools.product(a, b)]
    return Counter(m).most_common()[0][1] if m else 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0]], [[0]]),
    ([[1]], [[1]]),
    ([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]),
  ]
  rslts = [solver.largestOverlap(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
