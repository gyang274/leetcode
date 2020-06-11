from typing import List
from collections import deque
from itertools import accumulate

import bisect

class Solution:
  def shortestSubarray(self, A: List[int], K: int) -> int:
    """TC: O(N^2), SC: O(N).
    """
    A = list(accumulate(A, initial=0))
    n = len(A)
    d = n + 1
    s = []
    for i, x in enumerate(A):
      k = bisect.bisect(s, (x - K, n + 1))
      if k > 0:
        d = min(i - max(list(zip(*s[:k]))[1]), d)
      bisect.insort(s, (x, i))
    return -1 if d == n + 1 else d

class Solution:
  def shortestSubarray(self, A: List[int], K: int) -> int:
    """TC: O(NlogN), SC: O(N).
    """
    A = list(accumulate(A, initial=0))
    n = len(A)
    d = n + 1
    s = []
    for i, x in enumerate(A):      
      # O(logN)
      k = bisect.bisect(s, (x - K, n + 1))
      if k > 0:
        d = min(i - s[k - 1][1], d)
      # amortized O(1)
      while s and s[-1][0] >= x:
        s.pop()
      s.append((x, i))
    return -1 if d == n + 1 else d

class Solution:
  def shortestSubarray(self, A: List[int], K: int) -> int:
    """TC: O(N), SC: O(N).
    """
    A = list(accumulate(A, initial=0))
    n = len(A)
    d = n + 1
    s = deque([])
    for i, x in enumerate(A):      
      # amortized O(1)
      k = -1
      while s and s[0][0] <= x - K:
        # popleft is ok, since once k is ok for i - k, then j - k > i - k, all j > i.
        _, k = s.popleft()
      if k > -1:
        d = min(i - k, d)
      # amortized O(1)
      while s and s[-1][0] >= x:
        s.pop()
      s.append((x, i))
    return -1 if d == n + 1 else d

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1], 1),
    ([1,2], 4),
    ([2,-1,2], 3),
    ([-28,81,-20,28,-29], 89),
  ]
  rslts = [solver.shortestSubarray(A, K) for A, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")