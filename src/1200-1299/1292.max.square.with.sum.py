from typing import List

class Solution:
  def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
    # matrix augment with extra row and col of zeros
    mat = [[0] * (len(mat[0]) + 1)] + [[0] + r for r in mat]
    # O(MN), accumulative sum
    m, n = len(mat), len(mat[0])
    for i in range(1, m):
      for j in range(1, n):
        mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1]
    # O(MN), amortized O(1) to find max k for (i, j) such that (i, j) - (i + k, j + k) <= threshold
    l = 0
    for i in range(1, m):
      j, k = 1, 0
      while j < n:
        while i + k < m and j + k < n and mat[i + k][j + k] - mat[i - 1][j + k] - mat[i + k][j - 1] + mat[i - 1][j - 1] <= threshold:
          k += 1
        l = max(l, k)
        j += 1
    for j in range(1, n):
      i, k = 1, 0
      while i < n:
        while i + k < m and j + k < n and mat[i + k][j + k] - mat[i - 1][j + k] - mat[i + k][j - 1] + mat[i - 1][j - 1] <= threshold:
          k += 1
        l = max(l, k)
        i += 1
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6),
    ([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4),
  ]
  rslts = [solver.maxSideLength(mat, threshold) for mat, threshold in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
