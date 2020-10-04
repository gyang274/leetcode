from typing import List
from collections import Counter

class Solution:
  def _createLMT(self, d):
    s = ""
    for x in range(9, 0, -1):
      s += str(x) * d[x]
    return s + str(0) * d[0] if s else "0" if d[0] else ""
  def largestMultipleOfThree(self, digits: List[int]) -> str:
    d, s = Counter(digits), sum(digits) % 3
    if s == 1:
      for x in [1, 4, 7]:
        if d[x] > 0:
          d[x] -= 1
          s -= 1
          break
      if s == 1:
        count = 2
        for x in [2, 2, 5, 5, 8, 8]:
          if d[x] > 0:
            d[x] -= 1
            count -= 1
            if count == 0:
              s -= 1
              break
    elif s == 2:
      for x in [2, 5, 8]:
        if d[x] > 0:
          d[x] -= 1
          s -= 1
          break
      if s == 2:
        count = 2
        for x in [1, 1, 4, 4, 7, 7]:
          if d[x] > 0:
            d[x] -= 1
            count -= 1
            if count == 0:
              s -= 1
              break
    return self._createLMT(d)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0],
    [1],
    [0,0],
    [0,1,2],
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.largestMultipleOfThree(digits) for digits in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
