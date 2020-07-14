from typing import List
from collections import defaultdict

class Solution:
  def countTriplets(self, A: List[int]) -> int:
    """TC: reduce O(N^3) => O(N^2) with hash, like in 3sum Q0015.
    """
    n, d = len(A), defaultdict(lambda: 0)
    for i in range(n):
      for j in range(n):
        d[A[i] & A[j]] += 1
    count = 0
    for x in A:
      for y in d:
        if x & y == 0:
          count += d[y]
    return count

class Solution:
  def countTriplets(self, A: List[int]) -> int:
    """TC: O(M * 2^16 * N), M = num of elements from A, more scalable when M > 3.
      dynamic programming, use the fact that 0 <= A[i] < 2^16.
    """
    x, k = max(A), 1
    while x:
      x >>= 1
      k += 1
    m, n = 3, 1 << k
    dp = [[0] * n for _ in range(m + 1)]
    dp[0][n - 1] = 1
    for i in range(1, m + 1):
      for j in range(n):
        for x in A:
          dp[i][j & x] += dp[i - 1][j]
    return dp[m][0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,1,3],
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.countTriplets(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
