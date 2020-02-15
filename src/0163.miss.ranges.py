from typing import List

class Solution:
  def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
    nums = [lower - 1] + nums + [upper + 1]
    i, n, m = 0, len(nums), []
    for i in range(1, n):
      if nums[i - 1] < nums[i] - 1:
        m.append(str(nums[i] - 1) if nums[i - 1] == nums[i] - 2 else str(nums[i - 1] + 1) + '->' + str(nums[i] - 1))
      i += 1
    return m
    
if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([0, 1, 3, 50, 75], 0, 99),
  ]
  rslts = [solver.findMissingRanges(nums, lower, upper) for nums, lower, upper in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  