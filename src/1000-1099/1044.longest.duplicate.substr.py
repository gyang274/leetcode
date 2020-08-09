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
  def longestDupSubstring(self, S: str) -> str:
    # binary search + rabin karp (rolling hash), O(NlogN)
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
    x = ""
    if l > 0:
      i = self.hasDupSubStrLenK(s, l, n)
      x = S[i:(i + l)]
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "abcd",
    "banana",
  ]
  rslts = [solver.longestDupSubstring(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
