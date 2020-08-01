from typing import List
from itertools import product

class Solution:
  def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
    dwb = sorted((abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]), i, j) for (i, worker), (j, bike) in product(enumerate(workers), enumerate(bikes)))
    ans, ok = [-1] * len(workers), [True] * len(bikes)
    count = 0
    for _, i, j in dwb:
      if ans[i] < 0 and ok[j]:
        ans[i] = j
        ok[j] = False
        count += 1
        if count == len(workers):
          return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,0],[2,1]], [[1,2],[3,3]]),
    ([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]),
  ]
  rslts = [solver.assignBikes(workers, bikes) for workers, bikes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
