from typing import List
from collections import Counter

class Solution:
  def longestArithSeqLength(self, A: List[int]) -> int:
    n, d = len(A), {}
    for j in range(n):
      for i in range(j):
        if A[i] != A[j]:
          d[(A[i], A[j])] = max(d.get((A[i], A[j]), 2), d.get((A[i] - (A[j] - A[i]), A[i]), 1) + 1)
    return max(list(d.values()) + list(Counter(A).values()))

class Solution:
  def longestArithSeqLength(self, A: List[int]) -> int:
    n, dp = len(A), {}
    for j in range(n):
      for i in range(j):
        dp[(j, A[j] - A[i])] = dp.get((i, A[j] - A[i]), 1) + 1
    return max(dp.values())

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [9,4,7,2,5,10],
  ]
  rslts = [solver.longestArithSeqLength(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
