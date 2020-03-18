from collections import Counter

class Solution:
  def findTheDifference(self, s: str, t: str) -> str:
    sc, tc = Counter(s), Counter(t)
    for k, v in tc.items():
      if (k not in sc and v == 1) or sc[k] == v - 1:
        return k