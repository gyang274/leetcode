from collections import defaultdict

class Solution:
  def __init__(self):
    self.memo = {}
    self.memo[""] = 0
  def strangePrinter(self, s: str) -> int:
    # divide and conquer
    if s not in self.memo:
      n = len(s)
      # d: character -> index seen
      d = defaultdict(list)
      d[s[0]] = [0]
      # dp: dp[i] = min(dp[i - 1] + 1, dp[i-last-seen] + self.strangePrinter(s[(index-s[i]-seen+1):i]))
      dp = [i + 1 for i in range(n)]
      for i in range(1, n):
        if s[i] == s[i - 1]:
          dp[i] = dp[i - 1]
        else:
          dp[i] = dp[i - 1] + 1
          for k in d[s[i]]:
            dp[i] = min(dp[i], dp[k] + self.strangePrinter(s[(k + 1):i]))
        d[s[i]].append(i)
      self.memo[s] = dp[n - 1]
    return self.memo[s]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "abcabc",
    "abcabcabcabc",
    "dfafdafaeafeafdafeafdadfad",
  ]
  rslts = [solver.strangePrinter(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
