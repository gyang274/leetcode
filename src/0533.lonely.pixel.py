from typing import List

import itertools

class Solution:
  def findBlackPixel(self, picture: List[List[str]], N: int) -> int:
    # rr, cc: rows and cols where counts of black is 1
    n, m, rotated = len(picture), len(picture[0]), list(zip(*picture))
    rr = [i for i in range(n) if picture[i].count("B") == N]
    cc = [i for i in range(m) if rotated[i].count("B") == N]
    # (r, c) are candidate positions
    count = 0
    for c in cc:
      cr = [r for r in rr if picture[r][c] == "B"]
      if len(cr) == N and all([picture[r] == picture[cr[0]] for r in cr]):
        count += N
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([
      ['W', 'B', 'W', 'B', 'B', 'W'],    
      ['W', 'B', 'W', 'B', 'B', 'W'],    
      ['W', 'B', 'W', 'B', 'B', 'W'],    
      ['W', 'W', 'B', 'W', 'B', 'W'],
    ], 3),
    ([
      ['W', 'B', 'W', 'B', 'B', 'W'],
      ['B', 'W', 'B', 'W', 'W', 'B'],
      ['W', 'B', 'W', 'B', 'B', 'W'],
      ['B', 'W', 'B', 'W', 'W', 'B'],
      ['W', 'W', 'W', 'B', 'B', 'W'],
      ['B', 'W', 'B', 'W', 'W', 'B']
    ], 3)
  ]
  rslts = [solver.findBlackPixel(picture, N) for picture, N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
