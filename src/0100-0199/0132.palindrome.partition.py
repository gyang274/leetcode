from collections import defaultdict

class Solution:
  def isPalindrome(self, s: str) -> bool:
    if not s in self.memo:
      if len(s) <= 1:
        self.memo[s] = True
      else:
        self.memo[s] = (s[0] == s[-1]) and self.isPalindrome(s[1:-1])
    return self.memo[s]
  def minCut(self, s: str) -> int:
    """dynamic programming.
      dp[i] represent the min cut of palindrome of s[:i], dp[0] = 0.
      at each i >= 1, init: dp[i] = dp[i - 1] + 1
      dp[i] = min(dp[i], dp[k - 1] + 1) if s[i] == s[k] and s[(k + 1):i] is palindrome, 0 <= k < i
    """
    # memorize each character position to get k s.t. s[i] == s[i - k] at each i, and memorize all palindrome seen
    sdict, self.memo = defaultdict(list), {}
    # set dp[0] = -1 for recursive back to no cut, so dp[0] + 1 = 0
    dp = [-1 for _ in range(len(s) + 1)]
    for i in range(len(s)):
      dp[i + 1] = dp[i] + 1
      if s[i] in sdict:
        for k in sdict[s[i]]:
          if self.isPalindrome(s[(k + 1):i]):
            dp[i + 1] = min(dp[k] + 1, dp[i + 1])
      sdict[s[i]].append(i)
    # set back dp[0] = 0 for return when len(s) == 0
    dp[0] = 0
    return dp[len(s)]

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "",
    "a",
    "aa",
    "ab",
    "aab",
    "aba",
    "aabba",
    "aababa",
    "aabbaa",
  ]
  rslts = [solver.minCut(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  