from typing import List

import itertools

class Solution:
  def findLonelyPixel(self, picture: List[List[str]]) -> int:
    # rr, cc: rows and cols where counts of black is 1
    n, m, rotated = len(picture), len(picture[0]), list(zip(*picture))
    rr = [i for i in range(n) if picture[i].count("B") == 1]
    cc = [i for i in range(m) if rotated[i].count("B") == 1]
    # (r, c) are candidate positions
    count = 0
    for r, c in itertools.product(rr, cc):
      if picture[r][c] == "B":
        count += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      ['W', 'W', 'B'],
      ['W', 'B', 'W'],
      ['B', 'W', 'W']
    ],
  ]
  rslts = [solver.findLonelyPixel(picture) for picture in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

