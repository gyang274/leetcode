from typing import List

import heapq

class Solution:
  def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
    heapq.heapify(A)
    for _ in range(K):
      heapq.heappush(A, -heapq.heappop(A))
    return sum(A)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 2),
    ([2,-3,-1,5,-4], 2),
  ]
  rslts = [solver.largestSumAfterKNegations(A, K) for A, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
