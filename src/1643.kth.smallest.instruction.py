from typing import List

import math

class Solution:
  def kthSmallestPath(self, destination: List[int], k: int) -> str:
    nV, nH = destination
    # 'H' x nH + 'V' * nV
    x, n = '', nH + nV
    while n > 0:
      if nH == 0:
        return x + 'V' * nV
      if nV == 0:
        return x + 'H' * nH
      # determins next is H or V
      fH = math.comb(n - 1, nH - 1)
      if k <= fH:
        x += 'H'
        nH -= 1
      else:
        x += 'V'
        nV -= 1
        k -= fH
      n -= 1
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2, 3], 1),
    ([2, 3], 2),
    ([2, 3], 3),
  ]
  rslts = [solver.kthSmallestPath(destination, k) for destination, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
