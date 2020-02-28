class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    """dynamic programming - Top down
    """
    memo = {}
    upper = max(len(word1), len(word2))
    def dp(word1, word2, i, j):
      if (word1, word2) in memo:
        return memo[(word1, word2)]
      elif word1 == word2:
        return 0
      else:
        while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
          i += 1
          j += 1
        n0 = n1 = n2 = upper
        # remove
        if i < len(word1):
          n0 = dp(word1[:i] + word1[(i + 1):], word2, i, j)
        # insert
        if j < len(word2):
          n1 = dp(word1[:i] + word2[j] + word1[i:], word2, i + 1, j + 1)
        # replace
        if i < len(word1) and j < len(word2):
          n2 = dp(word1[:i] + word2[j] + word1[(i + 1):], word2, i + 1, j + 1)
        memo[(word1, word2)] = 1 + min(n0, n1, n2)
        return memo[(word1, word2)]
    return dp(word1, word2, 0, 0)


class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    """dynamic programming - Bottom up
    """
    n, m = len(word1), len(word2)
    if n * m == 0:
      return n + m
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
      dp[i][0] = i
    for j in range(m + 1):
      dp[0][j] = j
    for i in range(1, n + 1):
      for j in range(1, m + 1):
        # source w.r.t. insert, remove, replace
        dp[i][j] = min(1 + dp[i][j - 1], 1 + dp[i - 1][j], dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1))
    return dp[n][m]


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("eat", "tea"),
    ("horse", "ros"),
    ("intention", "execution"),
  ]
  rslts = [solver.minDistance(word1, word2) for word1, word2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")