from typing import List
from collections import defaultdict

class Solution:
  def lenLongestFibSubseq(self, A: List[int]) -> int:
    # dynamic programming
    # dp(j, k) = dp(i, j) + 1 if A[i] + A[j] = A[k]
    n, s, dp = len(A), {x: i for i, x in enumerate(A)}, defaultdict(lambda: 2)
    for k in range(n):
      for j in range(k):
        if A[k] - A[j] in s:
          i = s[A[k] - A[j]]
          if i < j:
            dp[(j, k)] = dp[(i, j)] + 1
    return max(dp.values()) if dp else 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3,4,5,6,7,8],
  ]
  rslts = [solver.lenLongestFibSubseq(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
