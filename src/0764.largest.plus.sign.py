from typing import List

class Solution:
  def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
    """O(5N^2)
    """
    mines = set([(i, j) for i, j in mines])
    # dp: num of 1s from left, right, up, down
    dp = [[[0] * 4 for _ in range(N)] for _ in range(N)]
    # left
    for i in range(N):
      for j in range(N):
        if (i, j) not in mines:
          if j == 0 or (i, j - 1) in mines:
            dp[i][j][0] = 1
          else:
            dp[i][j][0] = dp[i][j - 1][0] + 1
    # right
    for i in range(N):
      for j in range(N - 1, -1, -1):
        if (i, j) not in mines:
          if j == N - 1 or (i, j + 1) in mines:
            dp[i][j][1] = 1
          else:
            dp[i][j][1] = dp[i][j + 1][1] + 1
    # up
    for j in range(N):
      for i in range(N):
        if (i, j) not in mines:
          if i == 0 or (i - 1, j) in mines:
            dp[i][j][2] = 1
          else:
            dp[i][j][2] = dp[i - 1][j][2] + 1
    # down
    for j in range(N):
      for i in range(N - 1, -1, -1):
        if (i, j) not in mines:
          if i == N - 1 or (i + 1, j) in mines:
            dp[i][j][3] = 1
          else:
            dp[i][j][3] = dp[i + 1][j][3] + 1
    # max(min(.))
    return max([min(dp[i][j]) for i in range(N) for j in range(N)])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, []),
    (1, [[0,0]]),
    (2, []),
    (3, []),
    (5, [[4,2]]),
  ]
  rslts = [solver.orderOfLargestPlusSign(N, mines) for N, mines in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
