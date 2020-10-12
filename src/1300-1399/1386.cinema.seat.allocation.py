from typing import List
from collections import defaultdict

class Solution:
  def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    count = 2 * n
    # seats taken by row
    d = defaultdict(set)
    for i, j in reservedSeats:
      d[i].add(j)
    # group of left, middle, right, both
    l, m, r, b = {2,3,4,5}, {4,5,6,7}, {6,7,8,9}, {2,3,4,5,6,7,8,9}
    for k in d:
      if b & d[k]:
        if (l & d[k]) and (m & d[k]) and (r & d[k]):
          count -= 2
        else:
          count -= 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, [[2,1],[1,8],[2,6]]),
    (4, [[4,3],[1,4],[4,6],[1,7]]),
    (3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]),
  ]
  rslts = [solver.maxNumberOfFamilies(n, reservedSeats) for n, reservedSeats in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
