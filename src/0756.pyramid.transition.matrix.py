from typing import List
from collections import defaultdict

import itertools

class Solution:
  def recursive(self, row):
    n = len(row)
    if n == 1:
      return True
    candidates = []
    for i in range(n - 1):
      if row[i:(i + 2)] not in self.d:
        return False
      candidates.append(self.d[row[i:(i + 2)]])
    for r in itertools.product(*candidates):
      if self.recursive(''.join(r)):
        return True
    return False
  def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
    self.d = defaultdict(list)
    for triplet in allowed:
      self.d[triplet[:2]].append(triplet[2])
    return self.recursive(bottom)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("BCD", ["BCG", "CDE", "GEA", "FFF"]),
    ("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]),
  ]
  rslts = [solver.pyramidTransition(bottom, allowed) for bottom, allowed in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
