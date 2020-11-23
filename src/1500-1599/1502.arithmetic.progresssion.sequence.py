from typing import List

class Solution:
  def canMakeArithmeticProgression(self, nums: List[int]) -> bool:
    nums.sort()
    x = nums[1] - nums[0]
    for i in range(1, len(nums) - 1):
      if x != nums[i + 1] - nums[i]:
        return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.canMakeArithmeticProgression(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
