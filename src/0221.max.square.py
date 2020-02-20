from typing import List

class Solution:
  def maximalSquare(self, matrix: List[List[str]]) -> int:
    """refr Q0085, simplified to square.
      dynamic programming: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if matrix[i][j] == 1 else 0
    """
    n = len(matrix)
    if n == 0:
      return 0
    m = len(matrix[0])
    if m == 0:
      return 0
    # square side length, and dp framework
    rr, dp = 0, [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
      for j in range(1, m + 1):
        if matrix[i - 1][j - 1] == "1":
          dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
          rr = max(rr, dp[i][j])
    return rr * rr

class Solution:
  def maximalSquare(self, matrix: List[List[str]]) -> int:
    """refr Q0085, simplified to square.
      dynamic programming: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if matrix[i][j] == 1 else 0
      improvement: 2d to 1d as only previous row needed, update the same list as going through the new row.
    """
    n = len(matrix)
    if n == 0:
      return 0
    m = len(matrix[0])
    if m == 0:
      return 0
    # square side length, previous side length, and dp framework
    # previous side length: hold dp[i-1][j-1] for dp[i][j] when dp[i][j-1] overwrite it
    rr, prev, dp = 0, 0, [0] * (m + 1)
    for i in range(n):
      for j in range(1, m + 1):
        hold = dp[j]
        if matrix[i][j - 1] == "1":
          dp[j] = min(prev, dp[j - 1], dp[j]) + 1
        else:
          dp[j] = 0
        prev = hold
        rr = max(rr, dp[j])
    return rr * rr

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      ["1"]
    ],
    [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ],
    [
      ["0","0","0","1","0","1","1","1"],
      ["0","1","1","0","0","1","0","1"],
      ["1","0","1","1","1","1","0","1"],
      ["0","0","0","1","0","0","0","0"],
      ["0","0","1","0","0","0","1","0"],
      ["1","1","1","0","0","1","1","1"],
      ["1","0","0","1","1","0","0","1"],
      ["0","1","0","0","1","1","0","0"],
      ["1","0","0","1","0","0","0","0"]
    ],
    [
      ["0","1","1","0","0","1","0","1","0","1"],
      ["0","0","1","0","1","0","1","0","1","0"],
      ["1","0","0","0","0","1","0","1","1","0"],
      ["0","1","1","1","1","1","1","0","1","0"],
      ["0","0","1","1","1","1","1","1","1","0"],
      ["1","1","0","1","0","1","1","1","1","0"],
      ["0","0","0","1","1","0","0","0","1","0"],
      ["1","1","0","1","1","0","0","1","1","1"],
      ["0","1","0","1","1","0","1","0","1","1"]
    ],
  ]
  rslts = [solver.maximalSquare(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")