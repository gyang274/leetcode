from typing import Counter

import math

class Solution:
  def numWays(self, s: str) -> int:
    n = Counter(s)['1']
    if n % 3:
      return 0
    if n == 0:
      return math.comb(len(s) - 1, 2) % (10 ** 9 + 7)
    n1, n2 = n // 3, n // 3 * 2
    # <s1>1--0--1<s2>1--0--1<s3>
    i1s, i1t, i2s, i2t, k = -1, -1, -1, -1, 0
    for i, x in enumerate(s):
      if x == '1':
        k += 1
        if k == n1:
          i1s = i1t = i
        if k == n2:
          i2s = i2t = i
      else:
        if k == n1:
          i1t = i
        if k == n2:
          i2t = i
    return (i1t - i1s + 1) * (i2t - i2s + 1) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "000",
    "1101",
    "100001000001",
    "100100010100110",
  ]
  rslts = [solver.numWays(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
