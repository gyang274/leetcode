from typing import List
from collections import defaultdict

import itertools

class Solution:
  def subarraysDivByK(self, A: List[int], K: int) -> int:
    n, count = len(A), 0
    A = list(map(lambda x: x % K, itertools.accumulate(A)))
    d = defaultdict(lambda: 0)
    d[0] = 1
    for i in range(n):
      count += d[A[i]]
      d[A[i]] += 1
    return count

class Solution:
  def subarraysDivByK(self, A: List[int], K: int) -> int:
    n, s, d, k = len(A), 0, defaultdict(lambda: 0), 0
    d[0] = 1
    for x in A:
      s += x
      s %= K
      k += d[s]
      d[s] += 1
    return k

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 5),
    ([3,2,1,0,4], 8),
  ]
  rslts = [solver.subarraysDivByK(A, K) for A, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
