from typing import List

import bisect

class Solution:
  def sequentialDigits(self, low: int, high: int) -> List[int]:
    # 54 sequential digits including 1-9, or 45 if not.
    s = list(range(1, 10))
    for x in s:
      if x % 10 < 9:
        s.append(x * 10 + x % 10 + 1)
    return s[bisect.bisect_left(s, low):bisect.bisect_right(s, high)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (100, 300),
    (1000, 14000),
  ]
  rslts = [solver.sequentialDigits(low, high) for low, high in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
