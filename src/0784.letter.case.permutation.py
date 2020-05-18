from typing import List

import itertools

class Solution:
  def letterCasePermutation(self, S: str) -> List[str]:
    f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
    return list(map("".join, itertools.product(*map(f, S))))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "a1b2c",
  ]
  rslts = [solver.letterCasePermutation(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
