import sys
from typing import List


class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    result = sys.maxsize
    for i in range(len(nums) - 2):
      if i > 0 and nums[i] == nums[i-1]:
        continue
      j = i + 1
      k = len(nums) - 1
      while j < k:        
        s = nums[i] + nums[j] + nums[k]
        if abs(target - s) < abs(target - result):
          result = s
          if result == target:
            return result
        if s < target:
          j = j + 1
        else:
          k = k - 1
    return result


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([-1, 2, 1, -4], 1)
  ]
  rslts = [solver.threeSumClosest(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
