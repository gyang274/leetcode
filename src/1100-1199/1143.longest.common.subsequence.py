class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    """Q0712, dynamic programming
      dp[i][j]: max common subseq of text1[:i] and text2[:j]
      note: space optimization by keeping only last two rows
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if text1[i - 1] == text2[j - 1]:
          dp[i][j] = dp[i - 1][j - 1] + 1
        else:
          dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("sea", "eat"),
    ("delete", "leetcode"),
  ]
  rslts = [solver.longestCommonSubsequence(text1, text2) for text1, text2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
