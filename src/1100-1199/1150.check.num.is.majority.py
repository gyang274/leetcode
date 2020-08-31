from typing import List

import bisect

class Solution:
  def isMajorityElement(self, nums: List[int], target: int) -> bool:
    i, j, n = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target), len(nums)
    return i < n and j > 0 and nums[i] == nums[j - 1] == target and (j - i) > n // 2

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,2,3,3,3,4], 3),
    ([2,4,5,5,5,5,5,6,6], 5),
  ]
  rslts = [solver.isMajorityElement(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
