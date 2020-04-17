from collections import defaultdict

class Solution:
  def recursive(self, i, j):
    if (i, j) not in self.memo:
      if i > j:
        self.memo[(i, j)] = 0
      elif i == j:
        self.memo[(i, j)] = 1
      else:
        if self.s[i] == self.s[j]:
          self.memo[(i, j)] = self.recursive(i + 1, j - 1) + 2
        else:
          self.memo[(i, j)] = max(self.recursive(i + 1, j), self.recursive(i, j - 1))
    return self.memo[(i, j)]
  def longestPalindromeSubseq(self, s: str) -> int:
    """dynamic programming: dp[i, j] = (dp[i + 1, j - 1] + 2) if s[i] == s[j] else max(dp[i + 1, j], dp[i, j - 1])
    """
    self.s, self.memo = s, {}
    return self.recursive(0, len(s) - 1)

class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    """dynamic programming: dp[i, j] = (dp[i + 1, j - 1] + 2) if s[i] == s[j] else max(dp[i + 1, j], dp[i, j - 1])
    """
    n = len(s)
    # dynamic programming
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
      dp[i][i] = 1
    for i in range(n - 1):
      dp[i][i + 1] = 2 if s[i] == s[i + 1] else 1
    for d in range(2, n):
      for i in range(n - d):
        j = i + d
        if s[i] == s[j]:
          dp[i][j] = dp[i + 1][j - 1] + 2
        else:
          dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]

class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    """dynamic programming: dp[i, j] = (dp[i + 1, j - 1] + 2) if s[i] == s[j] else max(dp[i + 1, j], dp[i, j - 1])
    """    
    if s == s[::-1]:
      return len(s)
    n = len(s)
    # dynamic programming with reduced space
    dp = [0] * n
    dp[0] = 1
    for j in range(1, n):
      dpnext = dp[:]
      dpnext[j] = 1
      for i in range(j - 1, -1, -1):
        if s[i] == s[j]:
          dpnext[i] = dp[i + 1] + 2
        else:
          dpnext[i] = max(dpnext[i + 1], dp[i])
      dp = dpnext
    return dp[0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "abcdeced",
  ]
  rslts = [solver.longestPalindromeSubseq(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")