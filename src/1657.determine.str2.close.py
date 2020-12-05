from collections import Counter

class Solution:
  def closeStrings(self, word1: str, word2: str) -> bool:
    d1, d2 = Counter(word1), Counter(word2)
    return sorted(d1.keys()) == sorted(d2.keys()) and sorted(d1.values()) == sorted(d2.values())
