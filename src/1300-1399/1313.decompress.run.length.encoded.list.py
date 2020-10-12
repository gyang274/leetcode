from typing import List
from itertools import chain

class Solution:
  def decompressRLElist(self, nums: List[int]) -> List[int]:
    return list(chain.from_iterable([nums[i + 1]] * nums[i] for i in range(0, len(nums), 2)))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3,5,8,23,42,85],
  ]
  rslts = [solver.decompressRLElist(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
