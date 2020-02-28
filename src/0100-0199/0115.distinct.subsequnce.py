from collections import defaultdict


class Solution:
  def numDistinct(self, s: str, t: str) -> int:
    """dynamic programming 2d: 
      dp[i][j] represents number of distinct w.r.t to s[:(j + 1)] and t[:(i + 1)]
      dp[i][j] = dp[i][j - 1] + (dp[i - 1][j - 1] if s[j] == t[i] else 0), loop over outer i and inner j.
    """
    if len(s) < len(t):
      return 0
    if len(s) == len(t):
      return 1 if s == t else 0
    dp = [[0] * len(s) for _ in range(len(t))]
    # init
    dp[0][0] = 1 if s[0] == t[0] else 0
    for j in range(1, len(s)):
      dp[0][j] = dp[0][j - 1] + (1 if s[j] == t[0] else 0)
    for i in range(1, len(t)):
      for j in range(i, len(s)):
        dp[i][j] = dp[i][j - 1]
        if s[j] == t[i]:
          dp[i][j] += dp[i - 1][j - 1]
    return dp[len(t) - 1][len(s) - 1]


class Solution:
  def numDistinct(self, s: str, t: str) -> int:
    """dynamic programming 1d:
      dp[i] represents number of distinct w.r.t to s[:(j + 1)] and t[:(i + 1)], loop over j and keep status of i only.
    """
    cidx = defaultdict(list)
    for i in range(len(t)):
      cidx[t[i]].append(i + 1)
    dp = [0] * (len(t) + 1)
    dp[0] = 1
    for x in s:
      for idx in cidx[x][::-1]:
        dp[idx] += dp[idx - 1]
    return dp[-1]


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("babag", "bag"),
    ("rabbbit", "rabbit"),
    ("babgbag", "bag"),
  ]
  rslts = [solver.numDistinct(s, t) for s, t in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")