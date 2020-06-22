from typing import List
from collections import Counter

class Solution:
  def uncommonFromSentences(self, A: str, B: str) -> List[str]:
    d = Counter((A + ' ' + B).split())
    return [x for x in d if d[x] == 1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("apple apple", "banana"),
    ("this apple is sweet", "this apple is sour"),
  ]
  rslts = [solver.uncommonFromSentences(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
