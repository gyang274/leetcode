from typing import List
from collections import defaultdict

class Solution:
  def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
    if not len(words1) == len(words2):
      return False
    d = defaultdict(set)
    for w1, w2 in pairs:
      d[w1].add(w2)
      d[w2].add(w1)
    for w1, w2 in zip(words1, words2):
      if not (w1 == w2 or w1 in d[w2]):
        return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["great","acting","skills"], ["fine","drama","talent"], [["great","fine"],["drama","acting"],["skills","talent"]]),
  ]
  rslts = [solver.areSentencesSimilar(words1, words2, pairs) for words1, words2, pairs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")