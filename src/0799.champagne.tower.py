class Solution:
  def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    # simulation..
    r, c = query_row, query_glass
    dp = [[0] * (i + 1) for i in range(r + 1)]
    dp[0][0] = poured
    for i in range(1, r + 1):
      dp[i][0] += max(0, (dp[i - 1][0] - 1) / 2)
      dp[i][i] += max(0, (dp[i - 1][i - 1] - 1) / 2)
      for j in range(1, i):
        dp[i][j] += max(0, (dp[i - 1][j - 1] - 1) / 2)
        dp[i][j] += max(0, (dp[i - 1][j] - 1) / 2)
    return min(1, dp[r][c])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 1, 1),
    (2, 1, 1),
    (23, 7, 4),
  ]
  rslts = [solver.champagneTower(poured, query_row, query_glass) for poured, query_row, query_glass in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
