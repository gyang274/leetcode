class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    """TC: O(MN), dynamic programming, longest common subsequence.
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if word1[i - 1] == word2[j - 1]:
          dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
    return m + n - 2 * dp[m][n]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("sea", "eat"),
  ]
  rslts = [solver.minDistance(word1, word2) for word1, word2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")