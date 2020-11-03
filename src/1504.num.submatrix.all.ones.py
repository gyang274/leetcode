from typing import List

class Solution:
  def numSubmat(self, mat: List[List[int]]) -> int:
    # TC: O(N^3), SC: O(N^2).
    m, n = len(mat), len(mat[0])
    # prep
    for i in range(m):
      for j in range(n - 2, -1, -1):
        # mat[i][j]: length of running 1s on this row.
        if mat[i][j]:
          mat[i][j] += mat[i][j + 1]
    # main
    count = 0
    for i in range(m):
      for j in range(n):
        # use mat[i][j] as top-left, count in O(1) of k x .. submatrix of all 1s.
        x = mat[i][j]
        for k in range(m - i):
          x = min(x, mat[i + k][j])
          if x:
            count += x
          else:
            break
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,1,1,1,1,1]],
    [[1,0,1],[0,1,0],[1,0,1]],
    [[1,0,1],[1,1,0],[1,1,0]],
    [[0,1,1,0],[0,1,1,1],[1,1,1,0]],
  ]
  rslts = [solver.numSubmat(mat) for mat in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
