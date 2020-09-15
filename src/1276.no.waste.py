from typing import List

class Solution:
  def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
    T, C = tomatoSlices, cheeseSlices
    if T & 1 or T < 2 * C or T > 4 * C:
      return []
    J = (T - 2 * C) // 2
    return [J, C - J]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (0, 0),
    (4, 1),
    (4, 2),
    (16, 7),
    (17, 4),
    (4, 17),
  ]
  rslts = [solver.numOfBurgers(tomatoSlices, cheeseSlices) for tomatoSlices, cheeseSlices in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
