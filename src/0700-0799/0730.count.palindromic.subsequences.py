class Solution:
  def countPalindromicSubsequences(self, S: str) -> int:
    """dynamic programming
      dp[i][j][k]: num of distinct palindrome with k = (x - ord('a')) format x-x between s[i:(j+1)]
    """
    n, kk = len(S), ['a', 'b', 'c', 'd']
    dp = [[[0] * 4 for _ in range(n)] for _ in range(n)]
    for j in range(n):
      for i in range(j, -1, -1):
        for k in range(4):
          if i == j:
            # base case: 'x': {'x'}
            if S[i] == kk[k]:
              dp[i][j][k] = 1
          else:
            if not S[i] == kk[k]:
              dp[i][j][k] = dp[i + 1][j][k]
            elif not S[j] == kk[k]:
              dp[i][j][k] = dp[i][j - 1][k]
            else:
              # s[i] == s[j] == kk[k]
              # base case: 'xx': {'x', 'xx'}
              dp[i][j][k] = 2
              if i + 1 < j:
                # general case: 'x---x': {'x', 'xx'} and all x + "unique none-empty palindrome s[(i+1):(j-1+1)]" + x
                dp[i][j][k] += dp[i + 1][j - 1][0] + dp[i + 1][j - 1][1] + dp[i + 1][j - 1][2] + dp[i + 1][j - 1][3]
                dp[i][j][k] %= 1000000007
    return sum(dp[0][n - 1]) % 1000000007