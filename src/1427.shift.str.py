from typing import List

class Solution:
  def stringShift(self, s: str, shift: List[List[int]]) -> str:
    # accumulate and shift all at once
    m = 0
    for d, x in shift:
      m += (1 if d ^ 1 else -1) * x
    m %= len(s)
    return s[m:] + s[:m]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abc", [[0,1],[1,2]]),
    ("abcdefg", [[1,1],[1,1],[0,2],[1,3]]),
  ]
  rslts = [solver.stringShift(s, shift) for s, shift in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
