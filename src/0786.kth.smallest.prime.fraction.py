from typing import List

import heapq

class Solution:
  def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
    """Q0373, Q0378, priority queue + boundary explore.
    """
    n = len(A)
    seen, queue = {(0, n - 1)}, [(A[0] / A[-1], 0, n - 1)]
    for _ in range(K):
      r, i, j = heapq.heappop(queue)
      if i + 1 < j:
        if (i + 1, j) not in seen:
          seen.add((i + 1, j))
          heapq.heappush(queue, (A[i + 1] / A[j], i + 1, j))
        if (i, j - 1) not in seen:
          seen.add((i, j - 1))
          heapq.heappush(queue, (A[i] / A[j - 1], i, j - 1))
    return A[i], A[j]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,5], 3),
    ([1,7,23,29,47], 8),
  ]
  rslts = [solver.kthSmallestPrimeFraction(A, K) for A, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
