from typing import List
from collections import Counter
from functools import reduce

import operator

class Solution:
  def commonChars(self, A: List[str]) -> List[str]:
    # map reduce
    d = reduce(operator.__and__, map(Counter, A))
    # accumulate
    ans = []
    for k in d:
      ans.extend([k] * d[k])
    return ans

class Solution:
  def commonChars(self, A: List[str]) -> List[str]:
    return list(reduce(Counter.__and__, map(Counter, A)).elements())

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["cool","lock","cook"],
    ["bella","label","roller"],
  ]
  rslts = [solver.commonChars(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
