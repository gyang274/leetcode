from typing import List

class Solution:
  def checkPossibility(self, nums: List[int]) -> bool:
    d, n = 0, len(nums)
    for i in range(n - 1):
      if nums[i] > nums[i + 1]:
        if d > 0:
          return False
        if i > 0 and nums[i - 1] > nums[i + 1]:
          nums[i + 1] = nums[i]
        d += 1
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [4,2,1],
    [4,2,3],
    [3,4,2,3],
  ]
  rslts = [solver.checkPossibility(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
