from typing import List
from collections import Counter

class Solution:
  def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
    # reduce words in B to a single word M
    M = Counter()
    for b in map(Counter, B):
      for x in b:
        M[x] = max(M[x], b[x])
    def F(a):
      a = Counter(a)
      return all(a[x] >= M[x] for x in M)
    return list(filter(F, A))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["amazon","apple","facebook","google","leetcode"], ["e","o"]),
    (["amazon","apple","facebook","google","leetcode"], ["e","oo"]),
  ]
  rslts = [solver.wordSubsets(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
