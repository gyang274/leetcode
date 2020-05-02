class Solution:
  def minimumDeleteSum(self, s1: str, s2: str) -> int:
    """Q1143, dynamic programming
      dp[i][j]: min delete sum of s[:i] and s[:j]
      note: space optimization by keeping only last two rows
    """
    m, n = len(s1), len(s2)  
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
      dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
    for j in range(1, n + 1):
      dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if s1[i - 1] == s2[j - 1]:
          dp[i][j] = dp[i - 1][j - 1]
        else:
          dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
    return dp[m][n]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("sea", "eat"),
    ("delete", "leetcode"),
  ]
  rslts = [solver.minimumDeleteSum(s1, s2) for s1, s2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
