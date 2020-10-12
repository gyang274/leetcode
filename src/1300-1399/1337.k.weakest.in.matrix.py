from typing import List

import heapq

class Solution:
  def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    m, n = len(mat), len(mat[0])
    # ans: list of (num soliders, index)
    ans = []
    for i in range(m):
      for j in range(n):
        if mat[i][j] == 0:
          ans.append((j, i))
          break
      else:
        ans.append((n, i))
    heapq.heapify(ans)
    return [heapq.heappop(ans)[1] for _ in range(k)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,1,1,1],[1,1,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 2),
  ]
  rslts = [solver.kWeakestRows(mat, k) for mat, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
