from typing import List
from collections import deque
from itertools import accumulate

class Solution:
  def maxSubarraySumCircular(self, A: List[int]) -> int:
    n = len(A)
    # Kadane's algorithm: dynamic programming
    # dp[j] = max(A[i:(j + 1)], i < j), dp[j + 1] = A[j + 1] + max(dp[j], 0)
    ans = cur = float('-inf')
    for x in A:
      cur = x + max(cur, 0)
      ans = max(ans, cur)
    # ans is max(A[i:j]), still need A[:i] + A[j:] all i < j, -> max(A[:i], i < j) all j.
    l, r = list(accumulate(accumulate(A), max)), list(reversed(list(accumulate(reversed(A)))))
    for i in range(2, n):
      ans = max(ans, l[i - 2] + r[i])
    return ans

class Solution:
  def maxSubarraySumCircular(self, A: List[int]) -> int:
    n = len(A)
    # prefix sums + monoqueue
    # B = A + A, max(B[i:j], max(j - n, 0) <= i < j)
    q, s = deque([(-1, 0)]), list(accumulate(A + A))
    ans = float('-inf')
    for i, x in enumerate(s):
      # length <= n
      while q and i - q[0][0] > n:
        q.popleft()
      ans = max(ans, x - q[0][1])
      # if i1 < i2 and A[i1] >= A[i2], then (i2, A[i2]) is always preferred for j > i2
      while q and x <= q[-1][1]:
        q.pop()
      q.append((i, x))
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1],
    [4,-2,5],
    [2,3,1,1,4],
  ]
  rslts = [solver.maxSubarraySumCircular(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
