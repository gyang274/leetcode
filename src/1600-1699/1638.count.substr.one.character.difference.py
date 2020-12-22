class Solution:
  def countSubstrings(self, s: str, t: str) -> int:
    # dp, TC: O(MN), SC: O(MN * min(M, N))
    # dp[i][j][0] is true iff length k + 1 substr s[i:(i+k+1)] equals t[j:(j+k+1)]
    # dp[i][j][1] is true iff length k + 1 substr s[i:(i+k+1)] and t[j:(j+k+1)] has exact one mismatch
    m, n, K = len(s), len(t), min(len(s), len(t))
    dp = [[[True, False] for _ in range(n)] for _ in range(m)]
    count = 0
    for k in range(K):
      for i in range(m - k):
        for j in range(n - k):
          if s[i + k] != t[j + k]:
            dp[i][j][1] = dp[i][j][0]
            dp[i][j][0] = False
          if dp[i][j][1]:
            count += 1
    return count