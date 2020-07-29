from typing import List
from collections import defaultdict

class Solution:
  def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
    # d as color constraints
    d = defaultdict(set)
    for x, y in paths:
      d[max(x, y) - 1].add(min(x, y) - 1)
    # f as color of flower to plant
    f = [0] * N
    for i in range(N):
      f[i] = min(set([1,2,3,4]) - {f[j] for j in d[i]})
    return f

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [[1,2],[3,4]]),
    (3, [[1,2],[2,3],[3,1]]),
    (4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]),
  ]
  rslts = [solver.gardenNoAdj(N, paths) for N, paths in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
