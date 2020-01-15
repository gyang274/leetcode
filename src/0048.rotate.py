from typing import List


class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.

    Note 1 <= i <= n, 1 <= j <= n:
      A(i, j) -> A(j, n - i)
      A(j, n - i) -> A(n - i, n - j)
      A(n - i, n - j) -> A(n - j, i)
      A(n - j, i) -> A(i, j)
    Rotate is closure within each 4 elements
    """
    n = len(matrix[0])
    for i in range((n + 1) // 2):
      for j in range(n // 2):
        matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]
        

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ], 
  ]
  rslts = [solver.rotate(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")