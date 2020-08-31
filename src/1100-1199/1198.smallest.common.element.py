from typing import List
from collections import defaultdict

import heapq

class Solution:
  def smallestCommonElement(self, mat: List[List[int]]) -> int:
    # O(MN + MNlogN)
    m, n = len(mat), len(mat[0])
    # d: x -> (i, j)
    d, q = defaultdict(list), []
    for i in range(m):
      d[mat[i][0]].append((i, 0))
      q.append(mat[i][0])
    # move to right only
    heapq.heapify(q)
    while len(d) > 1:
      x = heapq.heappop(q)
      while q[0] == x:
        x = heapq.heappop(q)
      for i, j in d[x]:
        if j + 1 == n:
          return -1
        d[mat[i][j+1]].append((i, j + 1))
        heapq.heappush(q, mat[i][j+1])
      d.pop(x)
    return q[0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]],
  ]
  rslts = [solver.smallestCommonElement(mat) for mat in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
