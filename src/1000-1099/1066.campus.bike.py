from typing import List

import heapq

class Solution:
  def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
    n, m = len(workers), len(bikes)
    # distance between worker i and bike j
    dist = lambda i, j: abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
    # priority queue (cost, worker, bikes)
    q, seen = [(0, 0, 0)], set()
    while q:
      # bbt: binary representation of bikes taken
      cost, i, brbt = heapq.heappop(q)
      if i == n:
        return cost
      if (i, brbt) not in seen:
        seen.add((i, brbt))
        for j in range(m):
          if brbt & (1 << j) == 0:
            heapq.heappush(q, (cost + dist(i, j), i + 1, brbt | (1 << j)))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,0],[2,1]], [[1,2],[3,3]]),
    ([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]),
  ]
  rslts = [solver.assignBikes(workers, bikes) for workers, bikes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
