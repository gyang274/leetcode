from typing import List
from itertools import combinations

class Solution:
  def satisifiable(self, r):
    x = [0] * self.n
    for i, j in r:
      x[i] += 1
      x[j] -= 1
    return not any(x)
  def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
    # 1 <= requests.length <= 16
    self.n = n
    m = len(requests)
    for i in range(m, 0, -1):
      for r in combinations(requests, i):
        if self.satisifiable(r):
          return i
    return 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, [[1,1]]),
    (5, [[0,1],[1,0],[1,2],[2,3],[3,4],[4,0]]),
  ]
  rslts = [solver.maximumRequests(n, requests) for n, requests in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
