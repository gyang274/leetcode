from typing import List

class Solution:
  def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
    a, b, c = sorted([a, b, c])
    xmin = ((c - b) > 1) + ((b - a) > 1)
    if xmin == 2:
      if c - b == 2 or b - a == 2:
        xmin = 1
    xmax = c - a - 2
    return [xmin, xmax]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3, 4),
    (2, 3, 5),
    (2, 7, 4),
    (2, 8, 5),
  ]
  rslts = [solver.numMovesStones(a, b, c) for a, b, c in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
