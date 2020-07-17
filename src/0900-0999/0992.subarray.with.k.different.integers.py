from typing import List
from collections import defaultdict, deque

class Solution:
  def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
    i, j, k, d, n, count = 0, 0, 0, defaultdict(deque), len(A), 0
    while j < n:
      # extend the window to K unique, lock the index
      while j < n and len(d) < K:
        d[A[j]].append(j)
        j += 1
      k = j - 1
      # extend the window while K unique, index locked
      while j < n and A[j] in d:
        d[A[j]].append(j)
        j += 1
      # shrink the window while K unique, index update
      while i < n and len(d) == K:
        count += j - k
        d[A[i]].popleft()
        if len(d[A[i]]) == 0:
          d.pop(A[i])
        else:
          k = max(k, d[A[i]][0])
        i += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,1,2,3], 2),
    ([1,2,1,3,4], 3),
    ([2,1,2,1,1], 3),
  ]
  rslts = [solver.subarraysWithKDistinct(A, K) for A, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
