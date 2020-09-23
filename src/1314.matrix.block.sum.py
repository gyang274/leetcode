from typing import List

class Solution:
  def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    def M(i, j):
      return mat[min(i, m - 1)][min(j, n - 1)] if i >= 0 and j >= 0 else 0
    for i in range(m):
      for j in range(n):
        mat[i][j] += M(i - 1, j) + M(i, j - 1) - M(i - 1, j - 1)
    ans = [[0] * n for _ in range(m)]
    for i in range(m):
      for j in range(n):
        ans[i][j] = M(i + K, j + K) - M(i - K - 1, j + K) - M(i + K, j - K - 1) + M(i - K - 1, j - K - 1)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,2,3],[4,5,6],[7,8,9]], 1),
    ([[1,2,3],[4,5,6],[7,8,9]], 2),
  ]
  rslts = [solver.matrixBlockSum(mat, K) for mat, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
