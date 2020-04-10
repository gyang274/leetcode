class Solution:
  def reverseStr(self, s: str, k: int) -> str:
    n, r = len(s), ""
    for z, i in enumerate(range(0, n, k)):
      if z & 1:
        r += s[i:(i + k)]
      else:
        r += s[i:(i + k)][::-1]
    return r
