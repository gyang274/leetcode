from typing import List
from collections import deque

class Solution:
  def smallestRange(self, nums: List[List[int]]) -> List[int]:
    queue = sorted([(val, idx) for idx, num in enumerate(nums) for val in num])
    return xmin, xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]],
  ]
  rslts = [solver.smallestRange(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
