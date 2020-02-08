class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    """Optimal structure - dynamic programming.
      dp(i, j) = isMatch(s[i:], p[j:])
    """
    # Top-Down Approach
    memo = {}
    def dp(i, j):
      if (i, j) not in memo:
        if j == len(p):
          ans = i == len(s)
        else:
          f = i < len(s) and p[j] in {s[i], '.'}
          if j + 1 < len(p) and p[j + 1] == '*':
            ans = dp(i, j+2) or (f and dp(i+1, j))
          else:
            ans = f and dp(i+1, j+1)
        memo[(i, j)] = ans
      return memo[(i, j)]
    return dp(0, 0)


class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    """Optimal structure - dynamic programming.
      dp(i, j) = isMatch(s[i:], p[j:])
    """
    # Bottom-Up Approach
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[-1][-1] = True
    for i in range(len(s), -1, -1):
      for j in range(len(p) - 1, -1, -1):
        f = i < len(s) and p[j] in {s[i], '.'}
        if j + 1 < len(p) and p[j + 1] == '*':
          dp[i][j] = dp[i][j+2] or (f and dp[i+1][j])
        else:
          dp[i][j] = f and dp[i+1][j+1]
    return dp[0][0]


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("", ""),
    ("a", ""),
    ("", "a"),
    ("a", "a"),
    ("a", "."),
    ("a", "a*"),
    ("aa", "a"),
    ("aa", "a*"),
    ("aa", ".*"),
    ("aab", "c*a*b"),
    ("mississippi", "mis*is*p*."),
  ]
  rslts = [solver.isMatch(s, p) for s, p in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  