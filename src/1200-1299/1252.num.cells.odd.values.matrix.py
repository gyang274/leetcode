from typing import List
from collections import defaultdict

class Solution:
  def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
    d = defaultdict(lambda: 0)
    for i, j in indices:
      d[(0, i)] += 1
      d[(1, j)] += 1
    count = 0
    for i in range(n):
      for j in range(m):
        count += (d[(0, i)] + d[(1, j)]) & 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 2, [[0,0],[1,1]]),
    (2, 3, [[0,1],[1,1]]),
  ]
  rslts = [solver.oddCells(n, m, indices) for n, m, indices in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
