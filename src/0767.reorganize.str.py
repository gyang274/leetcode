class Solution:
  def reorganizeString(self, S: str) -> str:
    n = len(S)
    s = sorted([(S.count(x), x) for x in set(S)])
    if s[-1][0] > (len(S) + 1) // 2:
      return ""
    a = []
    for c, x in s:
      a.extend([x] * c)
    r = [None] * n
    r[::2], r[1::2] = a[(n//2):], a[:(n//2)]
    return "".join(r)