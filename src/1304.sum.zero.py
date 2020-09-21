from typing import List
from itertools import chain

class Solution:
  def sumZero(self, n: int) -> List[int]:
    return ([0] if n & 1 else []) + list(chain.from_iterable([i, -i] for i in range(1, n // 2 + 1)))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.sumZero(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
