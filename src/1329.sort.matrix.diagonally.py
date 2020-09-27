from typing import List
from collections import defaultdict

class Solution:
  def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    d = defaultdict(list)
    for i in range(m):
      for j in range(n):
        d[i - j].append(mat[i][j])
    for k in d:
      d[k].sort()
      for l, i in enumerate(range(max(0, k), max(0, k) + len(d[k]))):
        mat[i][i - k] = d[k][l]
    return mat

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[3,3,1,1],[2,2,1,2],[1,1,1,2]],
  ]
  rslts = [solver.diagonalSort(mat) for mat in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")