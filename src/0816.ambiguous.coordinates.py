from typing import List

import itertools

class Solution:
  def _dot(self, x):
    nx = len(x)
    if nx == 1:
      sx = {x}
    elif x[0] == '0' and x[-1] == '0':
      sx = {}
    elif x[0] == '0':
      sx = {x[:1] + '.' + x[1:]}
    elif x[-1] == '0':
      sx = {x}
    else:
      sx = {x}
      for i in range(1, nx):
        sx.add(x[:i] + '.' + x[i:])
    return sx
  def ambiguousCoordinates(self, S: str) -> List[str]:
    # S
    S = S[1:-1]
    # n
    n = len(S)
    # s: split to (x, y)
    s = []
    for i in range(1, n):
      if (i > 1 and int(S[:i]) == 0) or (i < n - 1 and int(S[i:]) == 0):
        continue
      s.append((S[:i], S[i:]))
    # ans: add . into x, y
    ans = []
    for x, y in s:
      ans.extend('(' + dx + ', ' + dy + ')' for dx, dy in itertools.product(self._dot(x), self._dot(y)))
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "(100)", "(123)", "(0123)", "(00011)",
  ]
  rslts = [solver.ambiguousCoordinates(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
