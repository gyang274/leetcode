from typing import List

import itertools

class Solution:
  def numSpecial(self, mat: List[List[int]]) -> int:
    rr = [i for i, r in enumerate(mat) if sum(r) == 1]
    cc = [i for i, c in enumerate(zip(*mat)) if sum(c) == 1]
    return sum(1 for i, j in itertools.product(rr, cc) if mat[i][j] == 1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,0,0],[0,1,0],[0,0,1]],
    [[1,0,0],[0,0,1],[1,0,0]],
    [[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]],
    [[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
  ]
  rslts = [solver.numSpecial(mat) for mat in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
