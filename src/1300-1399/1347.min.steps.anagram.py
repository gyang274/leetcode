from collections import Counter

class Solution:
  def minSteps(self, s: str, t: str) -> int:
    sc, tc = Counter(s), Counter(t)
    return sum((tc - sc).values())
