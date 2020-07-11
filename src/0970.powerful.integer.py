from typing import List

import itertools

class Solution:
  def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
    sx, sy = [1], [1]
    if x > 1:
      while sx[-1] <= bound:
        sx.append(sx[-1] * x)
      sx.pop()
    if y > 1:
      while sy[-1] <= bound:
        sy.append(sy[-1] * y)
      sy.pop()
    return list(filter(lambda z: z <= bound, set(px + py for px, py in itertools.product(sx, sy))))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3, 42),
  ]
  rslts = [solver.powerfulIntegers(x, y, bound) for x, y, bound in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")