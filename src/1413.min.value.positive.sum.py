from typing import List
from itertools import accumulate

class Solution:
  def minStartValue(self, nums: List[int]) -> int:
    return abs(min(min(accumulate(nums)), 0)) + 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [-3,2,-3,4,2],
  ]
  rslts = [solver.minStartValue(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
