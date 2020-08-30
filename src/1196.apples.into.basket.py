from typing import List
from itertools import accumulate

class Solution:
  def maxNumberOfApples(self, arr: List[int]) -> int:
    xs, bound = list(accumulate(sorted(arr))), 5000
    for i, x in enumerate(xs):
      if x > bound:
        return i
    return len(arr)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [100,200,150,1000],
    [900,950,800,1000,700,800],
  ]
  rslts = [solver.maxNumberOfApples(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
