from typing import List

import bisect

class Solution:
  def findSpecialInteger(self, arr: List[int]) -> int:
    if len(arr) < 4:
      return arr[0]
    candidates = [arr[i] for i in range(0, len(arr), len(arr) // 4)]
    for x in candidates:
      if (bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)) * 4 > len(arr):
        return x
    return None

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,3,5,5,5,5,8,23],
  ]
  rslts = [solver.findSpecialInteger(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
