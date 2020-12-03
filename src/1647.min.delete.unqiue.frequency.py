from collections import Counter

class Solution:
  def minDeletions(self, s: str) -> int:
    q = sorted(Counter(s).values())
    d, c = set(), 0
    for x in q:
      while x in d:
        x -= 1
        c += 1
      if x > 0:
        d.add(x)
    return c
