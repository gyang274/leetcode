from typing import List
from itertools import product

class Solution:
  def expand(self, S: str) -> List[str]:
    s, i, n = [], 0, len(S)
    while i < n:
      if S[i] == "{":
        xs = []
        i += 1
        while S[i] != "}":
          if S[i] != ",":
            xs.append(S[i])
          i += 1
        s.append(sorted(xs))
      else:
        s.append([S[i]])
      i += 1
    return list(map(lambda L: ''.join(L), product(*s)))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "abcd",
    "{a,b}c{d,e}",
    "{a,b,c}{z,x,y}",
  ]
  rslts = [solver.expand(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
