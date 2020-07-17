from typing import List

import heapq

class Solution:
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    queue = list(map(lambda x: [x[0] * x[0] + x[1] * x[1], x], points))
    heapq.heapify(queue)
    return [heapq.heappop(queue)[1] for _ in range(K)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,3],[-2,2]], 1),
    ([[3,3],[5,-1],[-2,4]], 2),
  ]
  rslts = [solver.kClosest(points, K) for points, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
