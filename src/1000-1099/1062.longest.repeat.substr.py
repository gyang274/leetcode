class Solution:
  def longestRepeatingSubstring(self, S: str) -> int:
    # O(N^2)
    n = len(S)
    # dp[i][j], longest repeat substr length with S[i] match S[j], i < j
    dp = [[0] * n for _ in range(n)]
    # dp[i][j] = dp[i - 1][j - 1] + 1 if S[i] == S[j] else 0
    xmax = 0
    for j in range(n):
      for i in range(j):
        if S[i] == S[j]:
          dp[i][j] = dp[i - 1][j - 1] + 1
          xmax = max(xmax, dp[i][j])
    return xmax

class Solution:
  def hasDupSubStrLenK(self, s, k, n):
    # O(N), via rolling hash of substr length k
    # M: modulus to avoid overflow, could cause hash collision..
    M = 1 << 32
    # k == 0, corner case, return -1 as default
    if k == 0:
      return -1
    # hash substr length k, 1 <= k < n
    h, B = 0, pow(26, k, M)
    for i in range(k):
      h = (h * 26 + s[i]) % M
    # hashset of substr hash
    seen = {h}
    for i in range(k, n):
      h = (h * 26 - s[i - k] * B + s[i]) % M
      if h in seen:
        return i - (k - 1)
      seen.add(h)
    return -1
  def longestRepeatingSubstring(self, S: str) -> str:
    # O(NlogN), binary search + rabin karp (rolling hash), Q1044
    n, s = len(S), list(map(lambda x: ord(x) - ord('a'), S))
    l, r, h = 0, n - 1, 0
    # binary search, O(logN)
    while l < r:
      m = r - (r - l) // 2
      # check has duplicate substr of length m at each step O(N)
      h = self.hasDupSubStrLenK(s, m, n)
      if h > -1:
        l = m
      else:
        r = m - 1
    # # retrieve the str itself, O(N)
    # x = ""
    # if l > 0:
    #   i = self.hasDupSubStrLenK(s, l, n)
    #   x = S[i:(i + l)]
    # return x
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "aaaa",
    "abab",
    "abba",
    "abcd",
  ]
  rslts = [solver.longestRepeatingSubstring(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
