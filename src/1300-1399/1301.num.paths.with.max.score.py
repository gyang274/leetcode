from typing import List

class Solution:
  def pathsWithMaxScore(self, board: List[str]) -> List[int]:
    n = len(board)
    # overwrite E and S into 0
    board[0], board[-1] = '0' + board[0][1:], board[-1][:-1] + '0'
    # dp, TC: O(N^2), SC: O(N^2).
    # dp[i][j]: (max score, num paths with max score)
    # dp[i][j][0] = board[i][j] + max(dp[i + 1][j][0], dp[i][j + 1][0], dp[i + 1][j + 1][0])
    # dp[i][j][1] = count of such paths with max score from all 3 possible moves
    dp = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    dp[n][n][1] = 1
    for i in range(n - 1, -1, -1):
      for j in range(n - 1, -1, -1):
        if board[i][j] != 'X' and dp[i + 1][j][1] + dp[i][j + 1][1] + dp[i + 1][j + 1][1] > 0:
          ms = max(dp[i + 1][j][0], dp[i][j + 1][0], dp[i + 1][j + 1][0])
          dp[i][j][0] = int(board[i][j]) + ms
          if dp[i + 1][j][0] == ms: 
            dp[i][j][1] += dp[i + 1][j][1]
          if dp[i][j + 1][0] == ms:
            dp[i][j][1] += dp[i][j + 1][1]
          if dp[i + 1][j + 1][0] == ms:
            dp[i][j][1] += dp[i + 1][j + 1][1]
        dp[i][j][1] %= 10 ** 9 + 7
    return dp[0][0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["E23","2X2","12S"],
    ["E12","1X1","21S"],
    ["E11","XXX","11S"],
  ]
  rslts = [solver.pathsWithMaxScore(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
