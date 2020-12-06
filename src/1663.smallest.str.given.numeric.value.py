class Solution:
  def getSmallestString(self, n: int, k: int) -> str:
    s, k, i = [0] * n, k - n, 0
    while k > 0:
      s[i] += min(k, 25)
      k -= min(k, 25)
      i += 1
    return ''.join(chr(97 + x) for x in s[::-1])
