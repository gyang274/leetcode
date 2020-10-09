from typing import List

import bisect

class Solution:
  def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    r = sorted([float('-inf')] + arr2 + [float('inf')])
    count = 0
    for x in arr1:
      i = bisect.bisect_right(r, x)
      if x - r[i - 1] > d and r[i] - x > d:
        count += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([4,5,8], [14,9,1,8], 2),
  ]
  rslts = [solver.findTheDistanceValue(arr1, arr2, d) for arr1, arr2, d in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
